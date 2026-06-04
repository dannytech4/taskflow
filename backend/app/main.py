from fastapi import FastAPI

from app.routers.users import router as users_router
from app.models.user import User

app = FastAPI(
    title="TaskFlow API"
)

app.include_router(users_router)


@app.get("/")
def root():
    return {
        "message": "TaskFlow API"
    }