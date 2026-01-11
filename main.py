import os
import secrets
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from github import Auth, Github
from pydantic import BaseModel

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


class GroupInfo(BaseModel):
    project_id: str
    detail_link: str


class ExceptionInfo(BaseModel):
    type: str
    message: str


class EventInfo(BaseModel):
    log_message: str
    request_method: str
    request_url: str
    referrer: str
    user_agent: str
    service: str
    version: str
    response_status: str


class ErrorReportingWebhook(BaseModel):
    version: str
    subject: str
    group_info: GroupInfo
    exception_info: ExceptionInfo
    event_info: EventInfo


auth = Auth.Token(os.environ["GITHUB_PAT"])


@app.post("/", dependencies=[Depends(basic_auth)])
def report(report: ErrorReportingWebhook):
    with Github(auth=auth) as g:
        repo = g.get_repo("YunosukeY/error-report-to-github-sample")
        repo.create_issue(
            title=report.event_info.log_message,
            body=f"""エラー
```
{report.event_info.log_message}
```

[ログの詳細を確認]({report.group_info.detail_link})
""",
        )
