import aiohttp
from loging_config import setup_logging
setup_logging()
import logging
from settings import settings
import xml.etree.ElementTree as ET
from database.operations import save_news



class Parser:
    async def fetch_page(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
            
    async def parse(self):
        try:
            page_content = await self.fetch_page(settings.rbc_url)
            for item in ET.fromstring(page_content).findall('.//item'):
                await save_news({
                    'id': item.find('.//{https://www.rbc.ru}news_id').text,
                    'title': item.find('title').text,
                    'link': item.find('link').text,
                    'pub_date': item.find('pubDate').text,
                    'description': item.find('description').text,
                    'category': item.find('category').text,
                    'text': item.find(".//rbc_news:full-text", namespaces={'rbc_news': 'https://www.rbc.ru'}).text
                    })
        except Exception as error:
            logging.error(error, exc_info=True)
    
parser = Parser()