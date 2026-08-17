import pytest

from clients.api_client import ApiClient
from clients.db_client import DatabaseClient
from tests.data import URL, ACCESS_TOKEN, CREATE_USER_PAYLOAD


# api_clients
@pytest.fixture(scope="module")
def api_client_without_auth():
    return ApiClient(base_url=URL)

@pytest.fixture(scope="module")
def api_client_with_valid_auth():
    return ApiClient(base_url=URL, token=ACCESS_TOKEN)

@pytest.fixture(scope="module")
def api_client_with_invalid_auth():
    return ApiClient(base_url=URL, token="wrong-token")


# get users
@pytest.fixture()
def get_users_response(api_client_without_auth):
    return api_client_without_auth.get("users")


# get one existing user
@pytest.fixture()
def get_existing_user_response(api_client_without_auth):
    return api_client_without_auth.get("users/1")


# create user
@pytest.fixture()
def create_new_user(api_client_with_valid_auth):
    response = api_client_with_valid_auth.post("users", json = CREATE_USER_PAYLOAD)

    assert response.status_code == 201

    user = response.json()

    yield user

    cleanup_response = api_client_with_valid_auth.delete(f"users/{user['id']}")

    # cleanup created user after the test
    if cleanup_response.status_code not in (204, 404):
        raise AssertionError(
            f"Cleanup failed: {cleanup_response.status_code}"
        )


#database
@pytest.fixture(scope="module")
def db_client():
    db_client = DatabaseClient()

    yield db_client

    db_client.close()

@pytest.fixture()
def db_created_user(db_client):
    user = db_client.create_user("New User", "new@new.new")

    yield user

    if db_client.get_user_by_id(user["id"]):
        db_client.delete_user(user["id"])