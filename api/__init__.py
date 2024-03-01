from fastapi import FastAPI
from api.routers import router as api_router 


def create_api() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    return app

app = create_api()