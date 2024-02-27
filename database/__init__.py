from tortoise import Tortoise

DB_CONFIG = {
    'connections': {
        'default': 'postgres://postgres:password@localhost:5432/application',
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
    async def setup():
        await Tortoise.init(DB_CONFIG)
        await Tortoise.generate_schemas()
        
    async def close():
        await Tortoise.close_connections()
        

