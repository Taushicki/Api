from binance.client import Client
from settings import settings

class BinanceParser:
    def __init__(self) -> None:
        self.client = Client(settings.binance_api_key, settings.binance_api_secret)
    
    async def return_symbol_ticker(self, symbol: str):
        return self.client.get_symbol_ticker(symbol=symbol)

    async def return_historical_klines(self, symbol: str):
        return self.client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1DAY, '1 month ago UTC')

binanceparser = BinanceParser()