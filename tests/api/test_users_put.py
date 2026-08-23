from tests.data import UPDATE_USER_PAYLOAD, UPDATE_USER_INVALID_NAME_TYPE, UPDATE_USER_INVALID_EMAIL_TYPE, \
    UPDATE_USER_PARTIAL_PAYLOAD_NAME


def test_replace_user_success(api_client_with_valid_auth, db_client, db_created_user):
    user_id = db_created_user["id"]

    response = api_client_with_valid_auth.put(f"users/{user_id}", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == UPDATE_USER_PAYLOAD["name"]
    assert data["email"] == UPDATE_USER_PAYLOAD["email"]
    assert data["id"] == user_id

    user_db = db_client.get_user_by_id(user_id)

    assert user_db == data


def test_replace_user_without_authorization_returns_401(api_client_without_auth):
    response = api_client_without_auth.put("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_replace_user_with_invalid_authorization_returns_401(api_client_with_invalid_auth):
    response = api_client_with_invalid_auth.put("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_replace_nonexisting_user_returns_404(api_client_with_valid_auth):
    response = api_client_with_valid_auth.put("users/1234567", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "User not found"


def test_replace_user_with_invalid_name_type_returns_422(api_client_with_valid_auth, db_created_user):
    user_id = db_created_user["id"]

    response = api_client_with_valid_auth.put(f"users/{user_id}", json=UPDATE_USER_INVALID_NAME_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "name"]


def test_replace_user_with_invalid_email_type_returns_422(api_client_with_valid_auth, db_created_user):
    user_id = db_created_user["id"]

    response = api_client_with_valid_auth.put(f"users/{user_id}", json=UPDATE_USER_INVALID_EMAIL_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "email"]


def test_replace_user_with_partial_payload_returns_422(api_client_with_valid_auth, db_created_user):
    user_id = db_created_user["id"]

    response = api_client_with_valid_auth.put(f"users/{user_id}", json=UPDATE_USER_PARTIAL_PAYLOAD_NAME)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "email"]