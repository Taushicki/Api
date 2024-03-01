import asyncio
from loging_config import setup_logging
setup_logging()
import logging
from parser.rbc_parser import parser
from parser.binance_parser import binanceparser
from database.__init__ import DataBaseSettings


async def main():

    
    try:
        import uvicorn
        uvicorn.run('api:app', host='0.0.0.0', port=8000, reload=True)
        await DataBaseSettings.setup()
        await parser.parse()
        # print(await binanceparser.return_symbol_ticker('BTCRUB'))
        # print(await binanceparser.return_historical_klines('BTCRUB'))
    except Exception as error:
        logging.error(error, exc_info=True)
    finally:
        await DataBaseSettings.close()
        
    

if __name__ == '__main__':
    asyncio.run(main())