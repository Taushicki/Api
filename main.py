import asyncio
from parser.rbc_parser import parser

async def main():
    await parser.parse()


if __name__ == '__main__':
    asyncio.run(main())