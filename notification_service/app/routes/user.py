from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.user_service import login_user, create_user
from app.db.database import get_db
from app.models.user import User

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post('/login')
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = login_user(request.email, request.password, db)
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@router.post('/register', response_model=User)
async def register(user: User, db: Session = Depends(get_db)):
    try:
        new_user = create_user(user, db)
        return new_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")