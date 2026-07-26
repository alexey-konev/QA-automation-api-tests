import requests

from app.schemas import UserCreate
from tests.data import UPDATE_USER_PAYLOAD

url = "http://localhost:8000"

user = UserCreate(
    name="Alex",
    username="asd"
)

CREATE_USER_PAYLOAD = {
    "name": 123,
    "username": "new_user123"
}

response = requests.put(f"{url}/users/1234", json = UPDATE_USER_PAYLOAD)



print(response.json())



# print(user)
# print(type(user))
# print(user.model_dump())
# print(type(user.model_dump()))
# print(user.model_dump_json())
# print(type(user.model_dump_json()))


