from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader

from app.data import users
from app.schemas import UserCreate, UserResponse, UserUpdate
from app.services import check_authorization
from clients.db_client import DatabaseClient


app = FastAPI()
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)


def get_db_client():
    db_client = DatabaseClient()

    yield db_client

    db_client.close()


@app.get("/")
def root():
    return {"message": "Hello QA1 Automation!"}


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int, db_client: DatabaseClient = Depends(get_db_client)):

    user = db_client.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
    # for user in users:
    #     if user["id"] == user_id:
    #         return user




@app.post("/users", status_code=201)
def create_user(user: UserCreate, authorization: str = Depends(api_key_header), db_client: DatabaseClient = Depends(get_db_client)):

    check_authorization(authorization)

    new_user = db_client.create_user(user.name, user.email)

    return new_user

    # if not users:
    #     new_id = 1
    # else:
    #     new_id = max(existing_user["id"] for existing_user in users) + 1
    #
    # new_user = UserResponse(id=new_id, name=user.name, email=user.email)
    # users.append(new_user.model_dump())
    #
    # return new_user


@app.put("/users/{user_id}")
def replace_user(user_id: int, user: UserCreate, authorization: str = Depends(api_key_header), db_client: DatabaseClient = Depends(get_db_client)):

    check_authorization(authorization)

    updated_user = db_client.replace_user(user_id, user.name, user.email)

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user
    # for index, existing_user in enumerate(users):
    #     if existing_user["id"] == user_id:
    #         updated_user = UserResponse(
    #             id=user_id,
    #             name=user.name,
    #             email=user.email)
    #         users[index] = updated_user.model_dump()
    #         return updated_user
    #
    # raise HTTPException(
    #     status_code=404,
    #     detail="User not found"
    # )


@app.patch("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, authorization: str = Depends(api_key_header), db_client: DatabaseClient = Depends(get_db_client)):

    check_authorization(authorization)

    updated_user = db_client.update_user(user_id, user.name, user.email)

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user

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
def delete_user(user_id: int, authorization: str = Depends(api_key_header), db_client: DatabaseClient = Depends(get_db_client)):

    check_authorization(authorization)

    user = db_client.delete_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return None
    # for index, existing_user in enumerate(users):
    #     if existing_user["id"] == user_id:
    #         users.pop(index)
    #         return None

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )