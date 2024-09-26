from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated, Optional
from datetime import date

ConstrainedStrID = Annotated[str, StringConstraints(pattern="^UI[a-zA-Z0-9]{7}$")]
ConstrainedPhoneNumber = Annotated[str, StringConstraints(pattern="^[89][0-9]{7}$")]

class EmployeeCreate(BaseModel):
    name: str
    email_address: EmailStr
    phone_number: ConstrainedPhoneNumber
    gender: str
    cafe_name: str

class EmployeeRead(BaseModel):
    id: str
    name: str
    email_address: EmailStr
    phone_number: str
    gender: str
    cafe_name: Optional[str]
    days_worked: int 
