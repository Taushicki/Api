from dataclasses import dataclass
from environs import Env
import logging

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Settings:
    rbc_url: str
    

def get_settings(path: str):
    env = Env()
    env.read_env(path)
    try:
        return Settings(rbc_url=env.str('RBC_URL'))
    except Exception as error:
        logging.error(error)
        
    
settings = get_settings('input')
logging.debug(settings)