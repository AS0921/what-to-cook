from fastapi import FastAPI

APP_VERSION = "0.1.0"

app = FastAPI(title="Что приготовить")

@app.get("/")
def root():
    return {"message": "Сервис подбора блюд работает"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": APP_VERSION}