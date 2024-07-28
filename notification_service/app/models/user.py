from pydantic import BaseModel
from typing import  List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    firstName: str
    email: str
    password: str
    roles: List[str]
    lastName: str
    dob: datetime


class UserTable(BaseModel):
    id: Optional[str]=None
    firstName: Optional[str]=None
    email: str
    password: str
    roles: List[str]
    lastName: Optional[str]=None
    dob: datetime
    notifications: Optional[List[str]]=[]
    created_at: Optional[datetime]=None

class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    roles: List[str]
    notifications: List[str]
    created_at: datetime
    dob: datetime

    class Config:
        from_attributes = True



