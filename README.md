# Task Manager API

Простой сервис для управления задачами (CRUD) на FastAPI + SQLAlchemy.

## 🚀 Запуск

### Локально
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

### Через Docker
```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
