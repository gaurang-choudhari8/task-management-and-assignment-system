from pydantic import BaseModel
from datetime import datetime
from enums import ProjectPhase
from user_schema import UserLite
from task_schema import TaskBase

class ProjectBase(BaseModel):
    title: str
    description: str
    due_date: datetime
    phase: ProjectPhase
    contributors: list[UserLite]
    tasks: list[TaskBase]

class ProjectCreate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    created_at: datetime


class ProjectLite(BaseModel):
    title: str
    description: str | None = None
    phase: ProjectPhase