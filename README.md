# Reporter

Install

```
uv sync
```

Lint

```
ruff check --fix
```

Format

```
ruff format
```

Type check

```
ty check
```

Dev server

```
fastapi dev main.py
```

Test

```
curl -u test_username:test_password -X POST -H "Content-Type: application/json" -d "{}" http://127.0.0.1:8000
```

Deploy

```
gcloud run deploy github-reporter --source . --region asia-northeast1 --allow-unauthenticated
```
