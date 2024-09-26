from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import init_db, get_db
from routes import cafe_routes, employee_routes
from typing import Annotated
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the database
init_db()

# Include API routes
app.include_router(cafe_routes, prefix="/cafes")
app.include_router(employee_routes, prefix="/employees")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)