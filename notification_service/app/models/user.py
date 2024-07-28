from pydantic import BaseModel
from typing import  List, Optional
from datetime import datetime

class User(BaseModel):
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



