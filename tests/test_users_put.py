from tests.data import UPDATE_USER_PAYLOAD, UPDATE_USER_INVALID_NAME_TYPE, UPDATE_USER_INVALID_USERNAME_TYPE, \
    UPDATE_USER_PARTIAL_PAYLOAD_NAME


def test_update_user_returns_updated_user(api_client_with_valid_auth):

    response = api_client_with_valid_auth.put("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == UPDATE_USER_PAYLOAD["name"]
    assert data["username"] == UPDATE_USER_PAYLOAD["username"]
    assert data["id"] == 1


def test_update_user_without_authorization_returns_401(api_client_without_auth):
    response = api_client_without_auth.put("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_update_user_with_invalid_authorization_returns_401(api_client_with_invalid_auth):
    response = api_client_with_invalid_auth.put("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_update_nonexisting_user_returns_404(api_client_with_valid_auth):
    response = api_client_with_valid_auth.put("users/1234", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "User not found"


def test_update_user_with_invalid_name_type_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.put("users/1", json=UPDATE_USER_INVALID_NAME_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "name"]


def test_update_user_with_invalid_username_type_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.put("users/1", json=UPDATE_USER_INVALID_USERNAME_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "username"]


def test_update_user_with_partial_payload_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.put("users/1", json=UPDATE_USER_PARTIAL_PAYLOAD_NAME)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "username"]