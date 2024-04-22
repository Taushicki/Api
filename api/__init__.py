from fastapi import FastAPI
from api.routers.news import router as news_router 
from api.routers.user import router as user_router 
from database.__init__ import DataBaseSettings

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(news_router, prefix='/news', tags=['news'])
    app.include_router(user_router, prefix='/users', tags=['users'])
    DataBaseSettings.setup(app)
    return app

app = create_app()