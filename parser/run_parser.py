from parser.rbc_parser import parser
import asyncio

async def run():
    while True:
        await parser.parse()
        await asyncio.sleep(300)
