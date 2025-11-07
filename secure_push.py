import subprocess
import os
import sys
from openai import OpenAI

def get_code_diff():
    result = subprocess.run(["git", "show", "--format=", "--unified=0"], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def ask_gpt(diff):
    prompt = f"""
    You are a security-focused code reviewer.
    Review the following code diff for all potential security vulnerabilities, unsafe patterns, insecure usage, or bad practices.

    List each issue clearly. Include explanations and suggest secure alternatives where possible.

    Reply with 'OK' only if absolutely no issues are found.

    Code diff:
    {diff}
    """
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=300,
        )
        reply = res.choices[0].message.content.strip()
        return reply
    except Exception as e:
        print("GPT request failed:", e)
        return "ERROR"

def undo_last_commit():
    print("Removing last commit (keeping changes staged)...")
    subprocess.run(["git", "reset", "--soft", "HEAD~1"])

def run_security_review():
    diff = get_code_diff()
    if not diff:
        print("No code changes detected.")
        return True

    print(" Sending code diff to GPT-3.5 for review...")
    review = ask_gpt(diff)

    if review == "OK":
        print("GPT-3.5 says: OK")
        return True
    elif review == "ERROR":
        print("GPT review failed.")
        return False
    else:
        print("GPT-3.5 flagged issues:\n")
        print(review)
        choice = input("\nDo you still want to push? (yes/no): ").strip().lower()
        return choice == "yes"

if __name__ == "__main__":
    if run_security_review():
        subprocess.run(["git", "push"])
    else:
        undo_last_commit()
        print("Push aborted.")
