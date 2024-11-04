from fastapi import FastAPI
from database import engine
from models.user import Base

app = FastAPI()

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
