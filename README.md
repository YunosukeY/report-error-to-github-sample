# Reporter

Install

```
uv sync
```

Lint

```
uv run ruff check --fix
```

Format

```
uv run ruff format
```

Type check

```
uv run ty check
```

Dev server

```
uv run --env-file .env fastapi dev main.py
```

Test

```
curl -u test_username:test_password -X POST -H "Content-Type: application/json" --data-binary @payload.json http://127.0.0.1:8000
```

Deploy

```
gcloud run deploy github-reporter --source . --region asia-northeast1 --allow-unauthenticated --env-vars-file=.env
```

Report error

```
gcloud beta error-reporting events report --service test-service \
  --message "java.lang.TestError: msg
    at com.example.TestClass.test(TestClass.java:51)
    at com.example.AnotherClass(AnotherClass.java:25)"
```
