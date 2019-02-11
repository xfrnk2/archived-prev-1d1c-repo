from bs4 import BeautifulSoup
import requests

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.find_all('a'))
# print(soup.get_text())


URL = 'http://naver.com/'
response = requests.get(URL)
print(response.text)

# PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k

req = requests.get('https://naver.com')
source = req.text
soup2 = BeautifulSoup(source, 'html.parser')

top_list = soup2.select(
    "#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

# print(top_list[0].text)
for top in top_list:
    print(top.text)