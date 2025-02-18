import hashlib
from db_manager import execute_query, fetch_query

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    password_hash = hash_password(password)
    execute_query("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    print(f"✅ User {username} created.")

def authenticate_user(username, password):
    password_hash = hash_password(password)
    result = fetch_query("SELECT id FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
    return len(result) > 0

if __name__ == "__main__":
    create_user("testuser", "password123")
    print(authenticate_user("testuser", "password123"))
