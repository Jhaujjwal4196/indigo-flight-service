from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.user_service import login_user, create_user
from app.db.database import get_db
from app.models.user import UserCreate, UserResponse
from app.models.userTable import User
from typing import List

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post('/login', response_model=UserResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = login_user(request.email, request.password, db)
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    

    
@router.post('/register', response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(user, db)
        return new_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    


@router.get('/users', response_model=List[UserResponse])
async def get_users(db:Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        return users
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")