from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader

from app.data import users
from app.schemas import UserCreate, UserResponse, UserUpdate
from app.services import check_authorization

app = FastAPI()
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


@app.get("/")
def root():
    return {"message": "Hello QA1 Automation!"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.post("/users", status_code=201)
def create_user(user: UserCreate, authorization: str = Depends(api_key_header)):

    check_authorization(authorization)

    if not users:
        new_id = 1
    else:
        new_id = max(existing_user["id"] for existing_user in users) + 1

    new_user = UserResponse(id=new_id, name=user.name, email=user.email)
    users.append(new_user.model_dump())

    return new_user


@app.put("/users/{user_id}")
def replace_user(user_id: int, user: UserCreate, authorization: str = Depends(api_key_header)):

    check_authorization(authorization)

    for index, existing_user in enumerate(users):
        if existing_user["id"] == user_id:
            updated_user = UserResponse(
                id=user_id,
                name=user.name,
                email=user.email)
            users[index] = updated_user.model_dump()
            return updated_user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, authorization: str = Depends(api_key_header)):

    check_authorization(authorization)

    for existing_user in users:
        if existing_user["id"] == user_id:
            updated_fields = user.model_dump(exclude_unset=True)
            for key, value in updated_fields.items():
                existing_user[key] = value

            return UserResponse(**existing_user)

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, authorization: str = Depends(api_key_header)):

    check_authorization(authorization)

    for index, existing_user in enumerate(users):
        if existing_user["id"] == user_id:
            users.pop(index)
            return None

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )