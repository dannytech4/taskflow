from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text

from sqlalchemy.orm import relationship

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status_id = Column( Integer, ForeignKey("task_statuses.id"), nullable=False )
    user_id = Column( Integer, ForeignKey("users.id"), nullable=False )
    is_deleted = Column( Boolean, nullable=False, server_default=text("0") )
    created_at = Column( DateTime, nullable=False, server_default=text("GETDATE()") )
    updated_at = Column( DateTime, nullable=False, server_default=text("GETDATE()") )
    user = relationship("User")
    status = relationship("TaskStatus")