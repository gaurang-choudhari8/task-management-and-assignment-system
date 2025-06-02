from pydantic import BaseModel
from datetime import datetime
from user_schema import UserBase
from task_schema import TaskBase
from project_schema import ProjectBase
from __future__ import annotations

class CommentBase(BaseModel):
    content: str
    created_at: datetime
    user: UserBase
    task: TaskBase
    upvotes: int
    downvotes: int
    reply_to: CommentBase

class CommentCreate(CommentBase):
    pass

class CommentOut(CommentBase):
    pass