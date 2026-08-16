from tests.data import UPDATE_USER_PAYLOAD, UPDATE_USER_PARTIAL_PAYLOAD_NAME, UPDATE_USER_PARTIAL_PAYLOAD_EMAIL, \
    UPDATE_USER_INVALID_NAME_TYPE, UPDATE_USER_INVALID_EMAIL_TYPE


def test_patch_user_all_fields_returns_200(api_client_with_valid_auth):
    response = api_client_with_valid_auth.patch("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == UPDATE_USER_PAYLOAD["name"]
    assert data["email"] == UPDATE_USER_PAYLOAD["email"]
    assert data["id"] == 1


def test_patch_user_name_only_returns_200(api_client_with_valid_auth):
    existing_user = api_client_with_valid_auth.get("users/1").json()

    response = api_client_with_valid_auth.patch("users/1", json=UPDATE_USER_PARTIAL_PAYLOAD_NAME)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == UPDATE_USER_PARTIAL_PAYLOAD_NAME["name"]
    assert data["email"] == existing_user["email"]
    assert data["id"] == 1


def test_patch_user_email_only_returns_200(api_client_with_valid_auth):
    existing_user = api_client_with_valid_auth.get("users/1").json()

    response = api_client_with_valid_auth.patch("users/1", json=UPDATE_USER_PARTIAL_PAYLOAD_EMAIL)
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == existing_user["name"]
    assert data["email"] == UPDATE_USER_PARTIAL_PAYLOAD_EMAIL["email"]
    assert data["id"] == 1


def test_patch_user_without_authorization_returns_401(api_client_without_auth):
    response = api_client_without_auth.patch("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_patch_user_with_invalid_authorization_returns_401(api_client_with_invalid_auth):
    response = api_client_with_invalid_auth.patch("users/1", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_patch_nonexisting_user_returns_404(api_client_with_valid_auth):
    response = api_client_with_valid_auth.patch("users/1234", json=UPDATE_USER_PAYLOAD)
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "User not found"


def test_patch_user_with_invalid_name_type_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.patch("users/1", json=UPDATE_USER_INVALID_NAME_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "name"]


def test_patch_user_with_invalid_email_type_returns_422(api_client_with_valid_auth):
    response = api_client_with_valid_auth.patch("users/1", json=UPDATE_USER_INVALID_EMAIL_TYPE)
    data = response.json()

    assert response.status_code == 422
    assert data["detail"][0]["loc"] == ["body", "email"]


def test_patch_user_with_empty_payload(api_client_with_valid_auth):
    existing_user = api_client_with_valid_auth.get("users/1").json()


    response = api_client_with_valid_auth.patch("users/1", json={})
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == existing_user["name"]
    assert data["email"] == existing_user["email"]
    assert data["id"] == 1