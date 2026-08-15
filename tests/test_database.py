def test_get_user_from_db_by_email(db_client):
    user = db_client.get_user_by_email("alex@test.com")

    assert user is not None
    assert user["name"] == "Alex"
    assert user["email"] == "alex@test.com"


def test_create_user_db(db_client, db_created_user):

    assert db_created_user["name"] == "New User"
    assert db_created_user["email"] == "new@new.new"

    user = db_client.get_user_by_email(db_created_user["email"])

    assert db_created_user == user


def test_delete_user_db(db_client, db_created_user):
    deleted_user = db_client.delete_user(db_created_user["id"])

    assert db_created_user == deleted_user
    assert db_client.get_user_by_email(deleted_user["email"]) is None


