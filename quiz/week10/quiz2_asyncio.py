import asyncio
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://nipponsei.minglong.org/tracker/')
html = resp.text

bs = BeautifulSoup(html, 'html.parser')
my_titles = bs.select(' tr > td.name > a')


async def custom_sleep():
    await asyncio.sleep(2)


async def print_titles():
    for title in my_titles:
        print(title.text)
        print(title.get('href'))
        await custom_sleep()


loop = asyncio.get_event_loop()
loop.run_until_complete(print_titles())
loop.close()
