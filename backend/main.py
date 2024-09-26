from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import init_db
from routes import cafe_routes, employee_routes

app = FastAPI()

origins = [
    "https://cafemanagerproject.netlify.app",
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
    import sys

    host = sys.argv[1] if len(sys.argv) > 1 else "0.0.0.0"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000

    uvicorn.run(app, host=host, port=port, reload=True)