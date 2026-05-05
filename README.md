# SmartFlow AI

Каркас веб-приложения для управления задачами.

## Backend (FastAPI)
- REST API с префиксом `/api/v1`
- Модули: auth, tasks, categories, dashboard
- Mock модули: voice, notifications

## Запуск
```bash
docker compose up --build
```

## Основные endpoint'ы
- Auth: `/auth/register`, `/auth/login`, `/auth/refresh`, `/auth/logout`, `/auth/me`
- Tasks: `GET/POST/PATCH/DELETE /tasks`
- Categories: `GET/POST/PATCH/DELETE /categories`
- Dashboard: `/dashboard/stats`, `/dashboard/today`, `/dashboard/upcoming`
- Voice mock: `/voice/command`, `/voice/process`
- Notifications mock: `/notifications/test`, `/notifications/settings`
