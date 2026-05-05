# SmartFlow AI


Task management web app scaffold.

## Backend (FastAPI)
- REST API with prefix `/api/v1`
- Modules: auth, tasks, categories, dashboard
- Mock modules: voice, notifications

## Run
=======
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
=======
## Основные endpoint'ы
- Auth: `/auth/register`, `/auth/login`, `/auth/refresh`, `/auth/logout`, `/auth/me`
- Tasks: `GET/POST/PATCH/DELETE /tasks`
- Categories: `GET/POST/PATCH/DELETE /categories`
- Dashboard: `/dashboard/stats`, `/dashboard/today`, `/dashboard/upcoming`
- Voice mock: `/voice/command`, `/voice/process`
- Notifications mock: `/notifications/test`, `/notifications/settings`
