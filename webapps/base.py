from webapps.jobs import route_jobs
from webapps.users import route_users
from webapps.auth import route_login
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_jobs.router, prefix='', tags=['job-webapp'])
api_router.include_router(route_users.router, prefix='', tags=['user-webapp'])
api_router.include_router(route_login.router, prefix='', tags=['auth-webapp'])

