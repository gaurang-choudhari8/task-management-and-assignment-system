from enum import Enum

class UserRole(Enum):
    ADMIN = "Admin"
    DEVELOPER = "Developer"
    MANAGER = "Manager"

class User:
    __id_counter = 1

    def __init__(self, id:str, name: str, email: str, role: UserRole, phone: str | None = None ):
        self.__id = f"CMT{User.__id_counter:03d}"
        User.__id_counter += 1
        self.name=name
        self.__email=email
        self.phone=phone
        self.role=role


    def get_email(self)->str:
        return self.__email
    
    def __repr__(self):
        return f"<User {self.name} ({self.role.value})>"