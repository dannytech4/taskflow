from datetime import datetime
from pydantic import BaseModel


class TaskResponse(BaseModel):

    id: int
    title: str
    description: str | None
    status_id: int
    user_id: int
    is_deleted: bool
    created_at: datetime
    updated_at: datetime | None
    model_config = {
        "from_attributes": True
    }

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status_id: int
    user_id: int

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status_id: int
    user_id: int


class TaskResponseStatus(BaseModel):
    id: int
    title: str
    description: str | None
    status_id: int
    user_id: int
    is_deleted: bool
    created_at: datetime
    updated_at: datetime | None
    model_config = {
        "from_attributes": True
    }


    
