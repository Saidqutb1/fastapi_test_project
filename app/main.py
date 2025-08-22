from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router as task_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="2.0.0")
app.include_router(task_router)
