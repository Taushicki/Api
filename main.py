import asyncio
import uvicorn
from loging_config import setup_logging
setup_logging()
import logging
from parser.run_parser import run
from api.__init__ import app

async def main():
    while True:
        try:
            asyncio.create_task(run())
            uvicorn.run("api:app", host='0.0.0.0', port=8000, reload=True)
        except Exception as error:
            logging.error(error, exc_info=True)


if __name__ == '__main__':
    asyncio.run(main())