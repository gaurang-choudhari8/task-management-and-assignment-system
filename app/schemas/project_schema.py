from pydantic import BaseModel
from datetime import datetime
from enums import ProjectPhase
from user_schema import UserBase
from task_schema import TaskBase

class ProjectBase(BaseModel):
    title: str
    description: str
    created_date: datetime
    due_date: datetime
    phase: ProjectPhase
    contributors: UserBase
    tasks: TaskBase

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    pass