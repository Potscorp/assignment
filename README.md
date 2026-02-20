# Task Dashboard - Full Stack Web App

A production-ready task management application with JWT authentication.

## Tech Stack

- **Frontend:** React + Vite + TailwindCSS
- **Backend:** Django + DRF + SimpleJWT
- **Database:** PostgreSQL (SQLite for dev)

## Quick Start

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

## Features

- User registration & login (JWT)
- Create, edit, delete tasks
- Search & filter tasks
- Responsive UI

## API Endpoints

- `POST /api/auth/register/` - Register
- `POST /api/auth/login/` - Login
- `GET /api/users/me/` - Get profile
- `GET /api/tasks/` - List tasks (?q=search&status=pending)
- `POST /api/tasks/` - Create task
- `PUT /api/tasks/<id>/` - Update task
- `DELETE /api/tasks/<id>/` - Delete task

## View Database

```bash
python view_db_simple.py
```

## Deployment (Render)

### Backend
- Build: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
- Start: `gunicorn core.wsgi:application`
- Set env vars: `DATABASE_URL`, `SECRET_KEY`, `DEBUG=False`

### Frontend
- Build: `npm install && npm run build`
- Publish: `dist`
- Set: `VITE_API_BASE_URL=<backend-url>/api`
