import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from datetime import date, timedelta
import random

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

    with SessionLocal() as db:
        cafes_count = db.query(Cafe).count()
        employees_count = db.query(Employee).count()
        
        if cafes_count == 0 and employees_count == 0:
            seed_data(db)

def seed_data(db: Session):
    from models.cafe import Cafe
    from models.employee import Employee
    from services import employee_service
    # Example seed data for cafes
    cafes = [
        Cafe(
            name="Cafe One",
            description="A cozy cafe.",
            location="Location One",
            employees=2
        ),
        Cafe(
            name="Cafe Two",
            description="A popular spot.",
            location="Location Two",
            employees=3
        )
    ]
    
    # Add cafes to the session
    db.add_all(cafes)
    db.commit() 

    cafe_one = cafes[0] 
    cafe_two = cafes[1] 
    
    # Example seed data for employees
    employees = [
        Employee(
            id=employee_service.generate_employee_id(db),
            name="John",
            email_address="john@example.com",
            phone_number="82345678",
            gender='Male',
            cafe_id=cafe_one.id,
            start_date=date.today() - timedelta(days=random.randint(0, 30))
        ),
        Employee(
            id=employee_service.generate_employee_id(db),
            name="Jane",
            email_address="jane@example.com",
            phone_number="87654321",
            gender='Female',
            cafe_id=cafe_one.id,
            start_date=date.today() - timedelta(days=random.randint(0, 30))
        ),
        Employee(
            id=employee_service.generate_employee_id(db),
            name="Alice",
            email_address="alice@example.com",
            phone_number="83456789",
            gender='Female',
            cafe_id=cafe_two.id,
            start_date=date.today() - timedelta(days=random.randint(0, 30))
        ),
        Employee(
            id=employee_service.generate_employee_id(db),
            name="Bob",
            email_address="bob@example.com",
            phone_number="94567890",
            gender='Male',
            cafe_id=cafe_two.id,
            start_date=date.today() - timedelta(days=random.randint(0, 30))
        ),
        Employee(
            id=employee_service.generate_employee_id(db),
            name="Charlie",
            email_address="charlie@example.com",
            phone_number="95678901",
            gender='Male',
            cafe_id=cafe_two.id,
            start_date=date.today() - timedelta(days=random.randint(0, 30))
        )
    ]
    
    # Add employees to the session
    db.add_all(employees)
    
    # Commit the session to save data
    db.commit()
