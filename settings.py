from dataclasses import dataclass
from environs import Env
from loging_config import setup_logging
setup_logging()
import logging


@dataclass
class Settings:
    rbc_url: str
    binance_api_key: str
    binance_api_secret: str
    

def get_settings(path: str):
    env = Env()
    env.read_env(path)
    try:
        return Settings(rbc_url=env.str('RBC_URL'),
                        binance_api_key=env.str('BINANCE_API_KEY'),
                        binance_api_secret=env.str('BINANCE_API_SECRET'))
    except Exception as error:
        logging.error(error, exc_info=True)
        
    
settings = get_settings('input')
logging.debug(settings, exc_info=True)