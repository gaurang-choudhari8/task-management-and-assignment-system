from enum import Enum
from datetime import datetime
from user import User
from project import Project

class Status(Enum):
    TODO = "Todo"
    IN_PROGRESS = "In-Progress"
    COMPLETED = "Completed"
    ON_HOLD = "On-Hold"

class Type(Enum):
    STORY = "Story"
    FEATURE = "Feature"
    EPIC = "Epic"
    BUG_FIX = "Bug-Fix"
    ENHANCEMENT = "Enhancement"
    

class Task:
    __id_counter = 1
    
    def __init__(self, title: str, type: Type,status: Status,owner: User,project: Project, description: str | None = None, due_date: datetime | None = None):
        self.__id = f"CMT{Task.__id_counter:03d}"
        Task.__id_counter += 1
        self.title = title
        self.description = description
        self.type = type
        self.status = status
        self.created_at = datetime.now()
        self.due_date = due_date
        self.owner = owner
        self.project = project

    def get_id(self):
        return self.__id

    def is_overdue(self)->bool:
        if self.due_date is None:
            return False
        return datetime.now()>self.due_date
    
    def update_status(self, status: Status):
        self.status=status
    
    def __repr__(self):
        return f"<Task Title: {self.title}, Description: {self.description}, Type: {self.type.value}, Status: {self.status.value}, Created At: {self.created_at}, Due Date: {self.due_date}, Owner: {self.owner.name}, Project: {self.project.title}>"
    
