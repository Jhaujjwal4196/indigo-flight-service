from sqlalchemy.orm import Session
from app.models.user import  UserTable
from app.models.userTable import User
from fastapi import  HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import SQLAlchemyError



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def login_user(email: str, password: str, db: Session):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return user

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(user: UserTable, db: Session) -> User:
    try:
    
        db_user = db.query(User).filter(User.email == user.email).first()

        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        hashed_password = get_password_hash(user.password)

        print(user.firstName, user.lastName, user.email, user.dob, hashed_password)

        new_user = User(
            first_name=user.firstName,
            last_name=user.lastName,
            email=user.email,
            password=hashed_password,
            roles=user.roles,
            dob=user.dob
        )
        print(new_user)
        db.add({new_user})
        db.commit()  # Commit the transaction
        db.refresh(new_user)  # Refresh the instance to get the updated data
        return new_user

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error occurred while creating user: {e}")
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="An error occurred while creating the user.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
