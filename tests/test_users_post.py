from tests.data import CREATE_USER_PAYLOAD, CREATE_USER_INVALID_NAME_TYPE, CREATE_USER_INVALID_EMAIL_TYPE


def test_create_user_persists_user_in_db(api_client_with_valid_auth, db_client):
    response = api_client_with_valid_auth.post("users", json=CREATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == CREATE_USER_PAYLOAD["name"]
    assert data["email"] == CREATE_USER_PAYLOAD["email"]
    assert isinstance(data["id"], int)

    user_db = db_client.get_user_by_id(data["id"])

    assert user_db == data

    cleanup_response = api_client_with_valid_auth.delete(f"users/{data["id"]}")

    assert cleanup_response.status_code == 204


def test_created_user_exists(api_client_with_valid_auth, create_new_user):
    user = create_new_user

    response = api_client_with_valid_auth.get(f"users/{user["id"]}")
    data = response.json()

    assert response.status_code == 200
    assert user == data


def test_create_user_without_authorization_returns_401(api_client_without_auth):
    response = api_client_without_auth.post("users", json=CREATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_create_user_with_invalid_authorization_returns_401(api_client_with_invalid_auth):
    response = api_client_with_invalid_auth.post("users", json=CREATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_create_user_with_invalid_name_type_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.post("users", json=CREATE_USER_INVALID_NAME_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "name"]


def test_create_user_with_invalid_email_type_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.post("users", json=CREATE_USER_INVALID_EMAIL_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "email"]

