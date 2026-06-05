from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class TaskStatus(Base):
    __tablename__ = "task_statuses"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), nullable=False)