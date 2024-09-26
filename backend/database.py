import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Get a database session for use in FastAPI dependencies.

    This function provides a generator that yields a database session
    and ensures proper cleanup after the session is used.

    Yields:
        Session: A SQLAlchemy database session.

    Raises:
        Exception: Any exceptions raised during session usage will be propagated.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize the database by creating all tables.

    This function imports the necessary models and creates the tables
    defined in those models within the database.

    Raises:
        Exception: Any exceptions raised during table creation will be propagated.
    """
    from models.cafe import Cafe
    from models.employee import Employee
    Base.metadata.create_all(bind=engine)