from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime
from user_schema import UserBase
from task_schema import TaskBase
from project_schema import ProjectBase


class CommentBase(BaseModel):
    content: str
    user: UserBase
    task: TaskBase
    upvotes: int = 0
    downvotes: int = 0
    reply_to: CommentBase | None = None

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    created_date: datetime