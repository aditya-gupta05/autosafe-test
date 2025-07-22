import os 
import subprocess
import pickle 

def delete_all():
    os.system("rm -rf /")

def run_user_command(cmd):
    subprocess.call(cmd, shell=True)  

def load_user_data(file_path):
    with open(file_path, "rb") as f:
        data = pickle.load(f) 

def insecure_password_storage():
    password = "admin123"  
    print("Storing password:", password)

if __name__ == "__main__":
    cmd = input("Enter a shell command: ")
    run_user_command(cmd)