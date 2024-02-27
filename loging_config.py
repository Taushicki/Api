import logging

def setup_logging():
    logging.basicConfig(
        filename='logs.log',
        encoding='utf-8',
        filemode='w',
        level=logging.DEBUG,
        format=r"%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s"
    )
    