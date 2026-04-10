from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Purchase Transaction API")

app.include_router(router)