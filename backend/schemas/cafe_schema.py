from pydantic import BaseModel
from typing import Optional

class CafeCreate(BaseModel):
    name: str
    description: str
    logo: Optional[str] = None  
    location: str

class CafeRead(BaseModel):
    id: str
    name: str
    description: str
    logo: Optional[str] = None  
    location: str
    employees: int



