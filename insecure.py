# insecure.py
import subprocess

def insecure_run():
    command = input("Enter command: ")
    subprocess.run(command, shell=True)
