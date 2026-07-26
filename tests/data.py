URL = "http://localhost:8000"

ACCESS_TOKEN = "secret-token"


CREATE_USER_PAYLOAD = {
    "name": "New User",
    "username": "new_user123"
}

CREATE_USER_INVALID_NAME_TYPE = {
    "name": 777,
    "username": "new_user123"
}

CREATE_USER_INVALID_USERNAME_TYPE = {
    "name": "New User",
    "username": 333
}


UPDATE_USER_PAYLOAD = {
    "name": "Updated User",
    "username": "upd_user"
}

UPDATE_USER_INVALID_NAME_TYPE = {
    "name": 777,
    "username": "upd_user"
}

UPDATE_USER_INVALID_USERNAME_TYPE = {
    "name": "Updated User",
    "username": 333
}

UPDATE_USER_PARTIAL_PAYLOAD_NAME = {
    "name": "Only Name"
}

UPDATE_USER_PARTIAL_PAYLOAD_USERNAME = {
    "username": "Only Username"
}


