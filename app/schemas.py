from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=3, max_length=20)


class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    email: str = Field(min_length=3, max_length=20)


class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=20)
    email: str | None = Field(None, min_length=3, max_length=20)
