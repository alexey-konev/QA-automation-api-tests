URL = "http://localhost:8000"

ACCESS_TOKEN = "secret-token"


CREATE_USER_PAYLOAD = {
    "name": "New User",
    "email": "new_user123"
}

CREATE_USER_INVALID_NAME_TYPE = {
    "name": 777,
    "email": "new_user123"
}

CREATE_USER_INVALID_EMAIL_TYPE = {
    "name": "New User",
    "email": 333
}


UPDATE_USER_PAYLOAD = {
    "name": "Updated User",
    "email": "upd_user"
}

UPDATE_USER_INVALID_NAME_TYPE = {
    "name": 777,
    "email": "upd_user"
}

UPDATE_USER_INVALID_EMAIL_TYPE = {
    "name": "Updated User",
    "email": 333
}

UPDATE_USER_PARTIAL_PAYLOAD_NAME = {
    "name": "Only Name"
}

UPDATE_USER_PARTIAL_PAYLOAD_EMAIL = {
    "email": "Only Username"
}


