from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from datetime import datetime
from sqlalchemy import or_

from sqlalchemy.orm import Session
from app.models.user import User
from app.models.task_status import TaskStatus

from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskResponse
from app.schemas.task import TaskResponseStatus
from app.schemas.task import TaskCreate
from app.schemas.task import TaskUpdate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    status_id: int | None = None,
    user_id: int | None = None,
    search: str | None = None,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db)):

    query = (
        db.query(Task)
        .filter(Task.is_deleted == False)
    )

    if status_id is not None:
        query = query.filter(
            Task.status_id == status_id
        )
    if user_id is not None:
        query = query.filter(
            Task.user_id == user_id
        )
    if search:
        query = query.filter(
            or_(
                Task.title.contains(search),
                Task.description.contains(search)
            )
        )
    offset = (page - 1) * page_size
    query = query.order_by(Task.id)
    
    return (
        query
        .offset(offset)
        .limit(page_size)
        .all()
    )
@router.post(
    "/",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        status_id=task.status_id,
        user_id=task.user_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.is_deleted == False
        )
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    user = (
        db.query(User)
        .filter(User.id == task_data.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    status = (
        db.query(TaskStatus)
        .filter(TaskStatus.id == task_data.status_id)
        .first()
    )

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Task status not found"
        )

    task.title = task_data.title
    task.description = task_data.description
    task.status_id = task_data.status_id
    task.user_id = task_data.user_id
    task.updated_at = datetime.now()

    db.commit()
    db.refresh(task)

    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = (
    db.query(Task)
    .filter(
        Task.id == task_id,
        Task.is_deleted == False
    )
    .first()
)
    
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.is_deleted = True
    task.updated_at = datetime.now()
    
    db.commit()

    return {
        "message": "Task deleted successfully"
    }
