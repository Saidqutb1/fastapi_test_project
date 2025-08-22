import uuid
from sqlalchemy import Column, String, Enum
from .database import Base
import enum


class TaskStatus(str, enum.Enum):
    created = "created"
    in_progress = "in_progress"
    completed = "completed"  


class Task(Base):
    __tablename__ = "task"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.created, nullable=False)

    