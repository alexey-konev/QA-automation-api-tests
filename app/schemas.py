from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=3, max_length=255)


class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    email: str = Field(min_length=3, max_length=255)


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=100)
    email: str | None = Field(None, min_length=3, max_length=255)
