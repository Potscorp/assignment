# Quick Start

## Setup (5 minutes)

### 1. Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 2. Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Test
- Open http://localhost:5173
- Register: username, email, password
- Create tasks
- Search & filter

## View Database
```bash
python view_db_simple.py
```

## Troubleshooting

**Backend won't start:** Run `python manage.py migrate`

**Frontend won't start:** Run `npm install`

**Can't create tasks:** Check backend is running on port 8000

**CORS errors:** Verify `CORS_ALLOW_ALL_ORIGINS = True` in settings.py
