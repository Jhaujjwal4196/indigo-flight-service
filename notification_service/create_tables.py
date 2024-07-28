from sqlalchemy import create_engine
from app.models.userTable import Base  # Adjust the import according to your project structure

DATABASE_URL = "sqlite:///./test.db"  # Update this to your actual database URL

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

print("Tables created successfully")
