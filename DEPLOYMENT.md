# Quick Deployment Guide (Render)

## 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 2. Backend Deployment

### Create PostgreSQL Database
- New + → PostgreSQL → Free tier
- Copy **Internal Database URL**

### Create Web Service
- New + → Web Service → Connect GitHub repo
- **Root Directory:** `backend`
- **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command:** `gunicorn core.wsgi:application`
- **Environment Variables:**
  ```
  SECRET_KEY=your-secret-key
  DEBUG=False
  DATABASE_URL=postgresql://...
  ALLOWED_HOSTS=your-backend.onrender.com
  CORS_ALLOWED_ORIGINS=https://your-frontend.onrender.com
  ```

## 3. Frontend Deployment

### Create Static Site
- New + → Static Site → Connect GitHub repo
- **Root Directory:** `frontend`
- **Build Command:** `npm install && npm run build`
- **Publish Directory:** `dist`
- **Environment Variable:**
  ```
  VITE_API_BASE_URL=https://your-backend.onrender.com/api
  ```

## 4. Update Backend CORS
Update backend environment variable:
```
CORS_ALLOWED_ORIGINS=https://your-actual-frontend-url.onrender.com
```

## Done!
Visit your frontend URL and test the app.

**See RENDER_DEPLOY.md for detailed step-by-step guide.**
