import aiohttp
from bs4 import BeautifulSoup


class Parser:
    async def fetch_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
            
    async def parse(self):
        try:
            page_content = await self.fetch_page()
        except:
            pass