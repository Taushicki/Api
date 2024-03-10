from fastapi import FastAPI
from api.routers import router as api_router 
from database.__init__ import DataBaseSettings

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router)
    DataBaseSettings.setup(app)
    return app

app = create_app()