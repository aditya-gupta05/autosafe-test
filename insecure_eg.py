import os
import subprocess
import pickle
import hashlib
import sqlite3
import jwt

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "123456"

# Insecure password hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Dangerous deserialization
def load_user(data):
    return pickle.loads(data)

# Shell injection vulnerability
def run_command(cmd):
    subprocess.call(f"ls {cmd}", shell=True)

# SQL injection vulnerability
def get_user_info(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    return cursor.fetchone()

# Insecure JWT handling (no verification)
def decode_token(token):
    return jwt.decode(token, options={"verify_signature": False})
