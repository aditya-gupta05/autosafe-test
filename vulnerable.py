import os
import subprocess
import sqlite3
import pickle
import base64

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "123456"

# Dangerous use of eval
user_input = input("Enter math expression: ")
print("Result:", eval(user_input))

# Dangerous use of exec
code = input("Enter Python code to run: ")
exec(code)

# Subprocess with shell=True (vulnerable to shell injection)
filename = input("Enter filename to delete: ")
subprocess.call(f"rm -rf {filename}", shell=True)

# Unsafe SQL construction (SQL injection possible)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
user_id = input("Enter your ID: ")
query = f"SELECT * FROM users WHERE id = '{user_id}'"
cursor.execute(query)
print(cursor.fetchall())

# Insecure deserialization
pickled_data = input("Paste pickled user data (base64 encoded): ")
decoded = base64.b64decode(pickled_data)
user = pickle.loads(decoded)
print("Welcome,", user["name"])
