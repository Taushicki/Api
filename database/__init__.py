from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
DB_CONFIG = {
    'connections': {
        'default': 'postgres://postgres:password@localhost:5432/application'
    },
    'apps': {
        'models': {
            'models': ['database.models'],
            'default_connection': 'default'
        }
    },
    'databases': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'E:/Applications/PostGreSQL/16/data',
                'port': '5432',
                'user': 'postgres',
                'password': 'password',
                'database': 'application',
            }
        }
    }
}

class DataBaseSettings:
    def setup(app: FastAPI):
        register_tortoise(
            app,
            config=DB_CONFIG,
            modules={'models': ['database.models']},
            generate_schemas=True,
            add_exception_handlers=True,
        )
        

