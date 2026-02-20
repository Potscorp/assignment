# Deployment Checklist

## Pre-Deployment
- [ ] Code pushed to GitHub
- [ ] Render account created
- [ ] All features tested locally

## Backend Deployment
- [ ] PostgreSQL database created
- [ ] Internal Database URL copied
- [ ] Web Service created
- [ ] Root directory set to `backend`
- [ ] Build command configured
- [ ] Start command configured
- [ ] Environment variables set:
  - [ ] SECRET_KEY
  - [ ] DEBUG=False
  - [ ] DATABASE_URL
  - [ ] ALLOWED_HOSTS
  - [ ] CORS_ALLOWED_ORIGINS
- [ ] Backend deployed successfully
- [ ] Backend URL noted

## Frontend Deployment
- [ ] Static Site created
- [ ] Root directory set to `frontend`
- [ ] Build command configured
- [ ] Publish directory set to `dist`
- [ ] Environment variable set:
  - [ ] VITE_API_BASE_URL
- [ ] Frontend deployed successfully
- [ ] Frontend URL noted

## Post-Deployment
- [ ] Backend CORS updated with actual frontend URL
- [ ] Backend redeployed
- [ ] Frontend loads correctly
- [ ] Can register new account
- [ ] Can login
- [ ] Can create tasks
- [ ] Can edit tasks
- [ ] Can delete tasks
- [ ] Search works
- [ ] Filter works

## Optional
- [ ] Admin user created
- [ ] Custom domain configured
- [ ] Monitoring set up

## URLs
- Backend: ___________________________________
- Frontend: ___________________________________
- Database: (Internal only)

## Troubleshooting
If something fails, check:
1. Render dashboard logs
2. Environment variables
3. Build/Start commands
4. CORS configuration
5. Database connection

See RENDER_DEPLOY.md for detailed help.
