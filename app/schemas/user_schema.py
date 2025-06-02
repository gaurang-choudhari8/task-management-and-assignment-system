from enums import UserRole
from pydantic import BaseModel

class UserBase(BaseModel):    
    name : str
    email : str
    phone : str | None
    role : UserRole        

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    pass