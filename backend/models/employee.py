from sqlalchemy import Column, String, Date, Enum, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship, Session
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(String(9), primary_key=True)
    name = Column(String(10), nullable=False)
    email_address = Column(String(50), nullable=False)
    phone_number = Column(String(8), nullable=False)
    gender = Column(Enum('Male', 'Female'), nullable=False)
    cafe_id = Column(String(36), ForeignKey('cafes.id'))
    start_date = Column(Date, default=func.now(), nullable=False)
    
    __table_args__ = (UniqueConstraint('id', 'cafe_id', name='unique_cafe_per_employee'),)

    cafe = relationship("Cafe", back_populates="employees_relation")

    def reset_employee_days(self, db: Session):
        self.start_date=func.now()
        db.commit()
        