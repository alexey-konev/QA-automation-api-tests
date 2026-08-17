

def test_delete_user_removes_user_from_api_and_db(api_client_with_valid_auth, db_client, db_created_user):
    user_id = db_created_user["id"]

    response_delete = api_client_with_valid_auth.delete(f"users/{user_id}")
    assert response_delete.status_code == 204
    assert response_delete.content == b""

    response_get = api_client_with_valid_auth.get(f"users/{user_id}")
    assert response_get.status_code == 404

    assert db_client.get_user_by_id(user_id) is None


def test_delete_user_without_authorization_returns_401(api_client_without_auth):
    response = api_client_without_auth.delete("users/1")
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_delete_user_with_invalid_authorization_returns_401(api_client_with_invalid_auth):
    response = api_client_with_invalid_auth.delete("users/1")
    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Unauthorized"


def test_delete_nonexisting_user_returns_404(api_client_with_valid_auth):
    response = api_client_with_valid_auth.delete("users/1234567")
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "User not found"