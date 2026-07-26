from fastapi import HTTPException


def check_authorization(authorization):
    print("AUTHORIZATION:", authorization)
    if authorization == "secret-token":
        return True

    raise HTTPException(
        status_code=401,
        detail="Unauthorized"
    )