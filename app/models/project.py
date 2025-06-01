from datetime import datetime
from enum import Enum
from user import User
from task import Task
from task import Status

class Phase(Enum):
    BUSSINESS_DESIGN = "Business Design"
    PLANNING = "Planning"
    REQUIREMENTS = "Requirements Gathering"
    DESIGN = "Design"
    DEVELOPMENT = "Development"
    SIT = "SIT"
    UAT = "UAT"



class Project:
    __id_counter = 1
    
    def __init__(self, title: str, phase: Phase, tasks: list[Task] | None = None, contributors: list[User] | None = None, description: str | None = None, due_date: datetime | None = None):
        self.__id = f"CMT{Project.__id_counter:03d}"
        Project.__id_counter += 1
        self.title = title
        self.description = description
        self.created_date = datetime.now()
        self.due_date = due_date
        self.phase = phase
        self.contributors = contributors if contributors else []
        self.tasks = tasks if tasks else []

    def get_id(self):
        return self.__id

    def __repr__(self):
        return f"<Project Title: {self.title}, Description: {self.description}, Created Date: {self.created_date}, Due Date: {self.due_date}, Phase: {self.phase}>"
    
    def get_contributors(self):
        return self.contributors
    
    def add_contributors(self, contributors: User | list[User]):
        if isinstance(contributors,User):
            self.contributors.append(contributors)
        elif isinstance(contributors,list[User]):
            self.contributors.extend(contributors)
        else:
            raise TypeError

    def add_tasks(self, tasks: Task | list[Task]):
        if isinstance(tasks,Task):
            self.tasks.append(tasks)
        elif isinstance(tasks,list[Task]):
            self.tasks.extend(tasks)
        else:
            raise TypeError

    def get_tasks_by_status(self, status: Status):
        return [task for task in self.tasks if task.status == status]
    
    def get_overdue_tasks(self):
        return [task for task in self.tasks if task.is_overdue()]
    
    def remove_contributors(self, contributors: User | list[User]):
        if isinstance(contributors,User):
            self.contributors.remove(contributors)
        elif isinstance(contributors,list[User]):
            self.contributors.remove(contributors)
        else:
            raise TypeError

