from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app:FastAPI = FastAPI(
    title=settings.PROJECT_NAME,
    debug=settings.DEBUG,
)

# Adding router from docs endpoints incl.
app.include_router(router)