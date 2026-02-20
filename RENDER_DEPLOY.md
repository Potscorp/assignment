# Deploy to Render - Complete Guide

## Prerequisites
- GitHub account
- Render account (free): https://render.com

## Step 1: Push Code to GitHub

```bash
cd assignment
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/task-dashboard.git
git push -u origin main
```

## Step 2: Deploy Backend (Django)

### 2.1 Create PostgreSQL Database

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"PostgreSQL"**
3. Settings:
   - **Name:** `taskdb`
   - **Database:** `taskdb`
   - **User:** `taskdb_user`
   - **Region:** Choose closest to you
   - **Plan:** Free
4. Click **"Create Database"**
5. **Copy the "Internal Database URL"** (starts with `postgresql://`)

### 2.2 Create Web Service for Backend

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Settings:
   - **Name:** `task-dashboard-backend`
   - **Region:** Same as database
   - **Root Directory:** `backend`
   - **Environment:** `Python 3`
   - **Build Command:**
     ```
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command:**
     ```
     gunicorn core.wsgi:application
     ```
   - **Plan:** Free

4. **Environment Variables** (click "Advanced" → "Add Environment Variable"):
   ```
   SECRET_KEY = django-insecure-CHANGE-THIS-TO-RANDOM-STRING
   DEBUG = False
   DATABASE_URL = [paste Internal Database URL from step 2.1]
   ALLOWED_HOSTS = task-dashboard-backend.onrender.com
   CORS_ALLOWED_ORIGINS = https://task-dashboard-frontend.onrender.com
   ```

5. Click **"Create Web Service"**

6. Wait for deployment (5-10 minutes)

7. **Note your backend URL:** `https://task-dashboard-backend.onrender.com`

### 2.3 Test Backend

Visit: `https://task-dashboard-backend.onrender.com/admin`
- Should see Django admin login page

## Step 3: Deploy Frontend (React)

### 3.1 Create Static Site

1. Click **"New +"** → **"Static Site"**
2. Connect same GitHub repository
3. Settings:
   - **Name:** `task-dashboard-frontend`
   - **Region:** Same as backend
   - **Root Directory:** `frontend`
   - **Build Command:**
     ```
     npm install && npm run build
     ```
   - **Publish Directory:** `dist`
   - **Plan:** Free

4. **Environment Variable** (click "Advanced"):
   ```
   VITE_API_BASE_URL = https://task-dashboard-backend.onrender.com/api
   ```

5. Click **"Create Static Site"**

6. Wait for deployment (3-5 minutes)

7. **Note your frontend URL:** `https://task-dashboard-frontend.onrender.com`

## Step 4: Update Backend CORS

1. Go to your backend service on Render
2. Click **"Environment"**
3. Update `CORS_ALLOWED_ORIGINS`:
   ```
   CORS_ALLOWED_ORIGINS = https://task-dashboard-frontend.onrender.com
   ```
4. Click **"Save Changes"**
5. Backend will auto-redeploy

## Step 5: Test Your App

1. Visit: `https://task-dashboard-frontend.onrender.com`
2. Click **"Register"**
3. Create account
4. Create tasks
5. Test all features

## Step 6: Create Admin User (Optional)

1. Go to backend service on Render
2. Click **"Shell"** tab
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Enter username, email, password
5. Visit: `https://task-dashboard-backend.onrender.com/admin`

## Important Notes

### Free Tier Limitations
- Services sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- Database expires after 90 days (free tier)

### URLs Summary
- **Backend:** `https://task-dashboard-backend.onrender.com`
- **Frontend:** `https://task-dashboard-frontend.onrender.com`
- **Database:** Internal URL (not public)

### Troubleshooting

**Backend won't start:**
- Check logs in Render dashboard
- Verify `DATABASE_URL` is correct
- Ensure all environment variables are set

**Frontend can't connect:**
- Verify `VITE_API_BASE_URL` is correct
- Check `CORS_ALLOWED_ORIGINS` includes frontend URL
- Check browser console for errors

**Database errors:**
- Verify `DATABASE_URL` format
- Check database is active
- Ensure migrations ran in build command

**500 errors:**
- Check backend logs
- Verify `SECRET_KEY` is set
- Ensure `DEBUG=False`

## Redeployment

### Backend Changes
```bash
git add .
git commit -m "Update backend"
git push
```
Render auto-deploys on push.

### Frontend Changes
```bash
git add .
git commit -m "Update frontend"
git push
```
Render auto-deploys on push.

## Cost
- **Free Tier:** $0/month
  - 750 hours/month web service
  - 100 GB bandwidth
  - PostgreSQL 90 days

- **Paid Tier:** $7/month per service
  - Always on
  - More resources
  - No time limits

## Security Checklist
- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY`
- ✅ Specific `CORS_ALLOWED_ORIGINS`
- ✅ `ALLOWED_HOSTS` configured
- ✅ HTTPS enabled (automatic on Render)
- ✅ Database password protected

## Next Steps
1. Add custom domain (optional)
2. Set up monitoring
3. Configure backups
4. Add CI/CD pipeline
5. Implement caching

Your app is now live! 🎉
