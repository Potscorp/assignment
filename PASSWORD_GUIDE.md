# Password Management

## View User Accounts
```bash
python view_users.py
```
Shows usernames, emails, and password hashes (not actual passwords).

## Why Can't I See Passwords?
Passwords are **hashed** using PBKDF2 algorithm for security. This is a one-way encryption - the original password cannot be retrieved.

## Reset a Password

### Method 1: Django Command
```bash
cd backend
python manage.py changepassword <username>
```

### Method 2: Create New Superuser
```bash
cd backend
python manage.py createsuperuser
```

### Method 3: Django Shell
```bash
cd backend
python manage.py shell
```
Then:
```python
from django.contrib.auth.models import User
user = User.objects.get(username='testuser')
user.set_password('newpassword123')
user.save()
```

## Test Accounts
If you need test accounts, register new ones through the app:
- Go to http://localhost:5173
- Click "Register"
- Create account with known password
