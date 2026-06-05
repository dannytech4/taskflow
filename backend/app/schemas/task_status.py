from pydantic import BaseModel


class TaskStatusResponse(BaseModel):

    id: int

    name: str

    model_config = {
        "from_attributes": True
    }