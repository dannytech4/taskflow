from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task_status import TaskStatus
from app.schemas.task_status import TaskStatusResponse

router = APIRouter(
    prefix="/task-statuses",
    tags=["Task Statuses"]
)


@router.get(
    "/",
    response_model=list[TaskStatusResponse]
)
def get_task_statuses(
    db: Session = Depends(get_db)
):

    statuses = (
        db.query(TaskStatus)
        .all()
    )

    return statuses