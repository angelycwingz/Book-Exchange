from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from pydantic import EmailStr

# Database table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: EmailStr = Field(unique=True)
    college: str

    # One user can have many books
    books: list["Book"] = Relationship(back_populates="owner")


# request body for creating a user
class UserCreate(SQLModel):
    name: str
    email: str
    college: str

# response body
class UserRead(SQLModel):
    id: int
    name: str
    email: str
    college: str

# avoid circular import
from models.book import Book
User.model_rebuild()