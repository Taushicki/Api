from loging_config import setup_logging
import logging

setup_logging()

def handle_error(error: Exception):
    logging.error(error, exc_info=True)
    return {'Error': {error}}