import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Session
from database import Base

class Cafe(Base):
    __tablename__ = "cafes"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(10), nullable=False, unique=True)
    description = Column(String(256), nullable=False)
    logo = Column(String(255))
    location = Column(String(255), nullable=False)
    employees = Column(Integer, nullable=False)

    employees_relation = relationship("Employee", back_populates="cafe", cascade="all, delete-orphan")
    
    def increment_employees(self, db: Session):
        """Increment the number of employees by one."""
        self.employees += 1
        db.commit()

    def decrement_employees(self, db: Session):
        """Decrement the number of employees by one, ensuring it doesn't go below zero."""
        if self.employees > 0:
            self.employees -= 1
            db.commit()
        else:
            raise ValueError("Number of employees cannot be less than zero.")