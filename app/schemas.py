from pydantic import BaseModel
from typing import Optional
from .models import TaskStatus


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    passstatus: TaskStatus = TaskStatus.created


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskOut(TaskBase):
    id: str
    status: TaskStatus = TaskStatus.created

    class Config:
        from_attributes = True