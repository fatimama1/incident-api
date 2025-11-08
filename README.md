# Incidents API

Простой API-сервис для учёта инцидентов.

---

## Технологии
- Python 3.12
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker & Docker Compose
- Alembic

---

## Запуск

1. Клонировать репозиторий и перейти в директорию проекта:
```bash
git clone <repo_url>
cd <project_folder>
```

2. Создать .env на основе .env.example:
```bash
cp .env.example .env
```

3. Построить и поднять контейнеры через Makefile:
```
make run
```
Приложение будет доступно на: http://localhost:8000

---

## Эндпоинты


| Метод | URL                    | Описание                   |
| ----- | ---------------------- | -------------------------- |
| POST  | /incidents/            | Создать инцидент           |
| GET   | /incidents/            | Получить список инцидентов |
| PATCH | /incidents/{id}/status | Обновить статус инцидента  |


## Примеры запросов:

Создание инцидента:
```bash
curl -X POST http://localhost:8000/incidents/ \
    -H "Content-Type: application/json" \
    -d '{"description": "Самокат не в сети", "source": "operator"}'
```

Получение списка инцидентов:
```bash
curl http://localhost:8000/incidents/
```

Обновление статуса:
```bash
curl -X PATCH http://localhost:8000/incidents/1/status \
    -H "Content-Type: application/json" \
    -d '{"status": "resolved"}'
```

---

## Команды Makefile

|Команда|Описание|
|---|---|
|`make build`|Построить контейнеры|
|`make up`|Поднять контейнеры|
|`make down`|Остановить контейнеры|
|`make logs`|Смотреть логи веб-сервиса|
|`make shell`|Войти внутрь контейнера веб-приложения|
|`make lint`|Проверка кода (ruff, black, isort)|
|`make format`|Авто-форматирование кода|
|`make run`|Полный цикл: down → build → up → logs|
