import sqlite3
import os

db_path = os.path.join('backend', 'db.sqlite3')

if not os.path.exists(db_path):
    print("Database not found!")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=" * 60)
print("USER ACCOUNTS")
print("=" * 60)

cursor.execute("SELECT id, username, email, password FROM auth_user")
users = cursor.fetchall()

print(f"\nTotal Users: {len(users)}\n")

for user in users:
    print(f"ID: {user[0]}")
    print(f"Username: {user[1]}")
    print(f"Email: {user[2]}")
    print(f"Password Hash: {user[3][:50]}...")
    print("-" * 60)

print("\nNOTE: Passwords are hashed using PBKDF2 algorithm.")
print("Original passwords cannot be retrieved for security.")
print("\nTo reset a password:")
print("  cd backend")
print("  python manage.py changepassword <username>")
print("=" * 60)

conn.close()
