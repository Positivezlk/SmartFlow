# SmartFlow AI




Task management web app saffold.

## Backend (FastAPI)
- REST API with prefix `/api/v1`
- Modules: auth, tasks, categories, dashboard

- Voice and notifications modules included

## Run without Docker

### 1) Install dependencies
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Start FastAPI
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3) Open frontend
Open `frontend/index.html` in browser.

## Main endpoints
- Mock modules: voice, notifications

## Run
Каркас веб-приложения для управления задачами.

## Backend (FastAPI)
- REST API с префиксом `/api/v1`
- Модули: auth, tasks, categories, dashboard
- Mock модули: voice, notifications

## Запуск
```bash
docker compose up --build
```


## Main endpoints
## Основные endpoint'ы
- Auth: `/auth/register`, `/auth/login`, `/auth/refresh`, `/auth/logout`, `/auth/me`
- Tasks: `GET/POST/PATCH/DELETE /tasks`
- Categories: `GET/POST/PATCH/DELETE /categories`
- Dashboard: `/dashboard/stats`, `/dashboard/today`, `/dashboard/upcoming`
- Voice: `/voice/command`, `/voice/process`
- Notifications: `/notifications/test`, `/notifications/settings`
=======
- Voice mock: `/voice/command`, `/voice/process`
- Notifications mock: `/notifications/test`, `/notifications/settings`
