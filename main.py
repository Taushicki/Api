import asyncio
from loging_config import setup_logging
setup_logging()
import logging
from parser.rbc_parser import parser
from database.__init__ import DataBaseSettings


async def main():
    try:
        await DataBaseSettings.setup()
        await parser.parse()
    except Exception as error:
        logging.error(error, exc_info=True)
    finally:
        await DataBaseSettings.close()

if __name__ == '__main__':
    asyncio.run(main())