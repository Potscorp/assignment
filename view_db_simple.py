import sqlite3
import os

db_path = os.path.join('backend', 'db.sqlite3')

if not os.path.exists(db_path):
    print("Database not found! Run: cd backend && python manage.py migrate")
    exit(1)

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("=" * 60)
    print("DATABASE CONTENTS")
    print("=" * 60)
    
    # Users
    print("\nUSERS TABLE")
    print("-" * 60)
    cursor.execute("SELECT id, username, email, date_joined FROM auth_user")
    users = cursor.fetchall()
    print(f"Total Users: {len(users)}\n")
    for user in users:
        print(f"ID: {user[0]}")
        print(f"Username: {user[1]}")
        print(f"Email: {user[2]}")
        print(f"Date Joined: {user[3]}")
        print("-" * 60)
    
    # Tasks
    print("\nTASKS TABLE")
    print("-" * 60)
    cursor.execute("""
        SELECT t.id, t.title, t.description, t.status, t.created_at, u.username
        FROM tasks_task t
        JOIN auth_user u ON t.user_id = u.id
    """)
    tasks = cursor.fetchall()
    print(f"Total Tasks: {len(tasks)}\n")
    for task in tasks:
        print(f"ID: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Status: {task[3]}")
        print(f"Created: {task[4]}")
        print(f"User: {task[5]}")
        print("-" * 60)
    
    # Summary
    print("\nSUMMARY")
    print("-" * 60)
    cursor.execute("SELECT COUNT(*) FROM auth_user")
    user_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM tasks_task")
    task_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM tasks_task WHERE status='pending'")
    pending_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM tasks_task WHERE status='done'")
    done_count = cursor.fetchone()[0]
    
    print(f"Total Users: {user_count}")
    print(f"Total Tasks: {task_count}")
    print(f"Pending Tasks: {pending_count}")
    print(f"Done Tasks: {done_count}")
    print("=" * 60)
    
    conn.close()
    
except sqlite3.OperationalError as e:
    print(f"\nError: {e}")
    print("\nDatabase tables not created yet!")
    print("Run: cd backend && python manage.py migrate")
except Exception as e:
    print(f"\nError: {e}")
