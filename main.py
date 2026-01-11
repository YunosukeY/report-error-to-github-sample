import secrets
from typing import Annotated

from fastapi import Body, Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


def basic_auth(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    is_username_correct = secrets.compare_digest(credentials.username, "test_username")
    is_password_correct = secrets.compare_digest(credentials.password, "test_password")
    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Basic"},
        )


@app.post("/", dependencies=[Depends(basic_auth)])
def report(payload: dict = Body(...)):
    print(payload)
