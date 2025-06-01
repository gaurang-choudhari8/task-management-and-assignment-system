from __future__ import annotations 
from datetime import datetime
from user import User
from task import Task

class Comment:
    __id_counter = 1

    def __init__(self, id: str, content: str, created_at: datetime, user: User, task: Task, upvotes: int = 0, downvotes: int = 0, reply_to: Comment | None = None):
        self.__id = f"CMT{Comment.__id_counter:03d}"
        Comment.__id_counter += 1
        self.content = content
        self.created_at = created_at
        self.user = user
        self.task = task
        self.upvotes = upvotes
        self.downvotes = downvotes
        self.reply_to = reply_to

    def get_id(self):
        return self.__id


    def __repr__(self):
        return f"<Comment Content: {self.content}, Created At: {self.created_at}, User: {self.user.name}, Task: {self.task.title}, Upvotes: {self.upvotes}, Downvotes: {self.downvotes}, Reply to: {self.reply_to}>"

    def upvote(self):
        self.upvotes+=1

    def downvote(self):
        self.downvotes+=1

    def is_reply(self):
        self.reply_to is not None