

def test_delete_user_returns_204(api_client_with_valid_auth, create_new_user):
    user = create_new_user

    response_delete = api_client_with_valid_auth.delete(f"users/{user["id"]}")
    assert response_delete.status_code == 204
    assert response_delete.content == b""

    response_get = api_client_with_valid_auth.get(f"users/{user["id"]}")
    assert response_get.status_code == 404


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
    response = api_client_with_valid_auth.delete("users/1234")
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "User not found"