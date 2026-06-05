from fastapi import FastAPI

from app.routers.users import router as users_router
from app.models.user import User
from app.routers.task_statuses import router as task_statuses_router
from app.routers.tasks import router as tasks_router

app = FastAPI(
    title="TaskFlow API"
)

app.include_router(users_router)
app.include_router(task_statuses_router)
app.include_router(tasks_router)


@app.get("/")
def root():
    return {
        "message": "TaskFlow API"
    }