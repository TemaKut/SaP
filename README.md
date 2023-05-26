# SaP (Share a Project)
The site designed for programmers.

## Описание
Статус проекта: В разработке.

Проект создан по классической архитектуре web приложений (Backend и Frontend)

Backend: Написан на языке Python с использованием фреймворка FastAPI.
Сохранение данных происходит в БД PostgreSQL при помощи асинхронной ORM SQLAlchemy

Frontend: Написан на JavaScript с использованием библиотеки React. Используется паттерн проектирования Single Page Application

## Запуск проекта
Для запуска проекта используется docker-compose (В случае отсутствия docker на Вашем компьютере - его следует установить.)

1. Запустить backend и postgres:
В Docker-compose.yml указаны переменные env (Для простоты запуска можно оставить или сменить на актуальные)

Находясь в корневой директории проекта (../SaP/) выполнить следующие команды в терминале
```bash
docker-compose up -d --build
```

При выполнении этой команды запускается БД, Backend, а так же выполняются миграции

2. Запустить frontend
Изначально, находясь в корневой директории проекта (../SaP/) выполнить следующие команды в терминале
```bash
cd frontend
npm start
```

3. После запуска - будут зарезервированы следующие url:
Документация backend -> http://localhost:8000/docs
Frontend -> http://localhost:3000