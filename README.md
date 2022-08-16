Send email with FastAPI framework
---
env/.env file:
  - MAIL_USERNAME
  - MAIL_PASSWORD
---
To run app:
```
uvicorn app:app --reload
```
Dockerfile:
```
docker build -t send_email .
```
```
docker run -d --rm send_email
```