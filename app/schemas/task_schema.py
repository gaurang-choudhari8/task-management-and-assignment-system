from pydantic import BaseModel
from enums import TaskType, TaskStatus
from datetime import datetime
from user_schema import UserBase
from project_schema import ProjectBase

class TaskBase(BaseModel):
    title: str
    description: str
    type: TaskType
    status: TaskStatus
    created_at: datetime
    due_date: datetime
    owner: UserBase
    project: ProjectBase

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    pass