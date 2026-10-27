# Load the .env file
from dotenv import load_dotenv
load_dotenv()

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes import books, users

# Load the .env file
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    create_tables()
    print("Database tables created successfully.")
    yield
    print("Application shutdown")

app = FastAPI(
    title = "Kitab Exchange API",
    description = "A simple API for exchanging used books",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(users.router)
app.include_router(books.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Kitab Exchange API"}