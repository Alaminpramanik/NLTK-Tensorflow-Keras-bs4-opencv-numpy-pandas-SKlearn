import sys
import logging
from pysitemap import crawler
from bs4 import BeautifulSoup
import requests
import re


url = 'https://stylishnick.com/'
# text=''
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
#     }
# res = requests.get(url, headers=headers, timeout=30)
# text += res.text
#     # print('text ', text)
# content = BeautifulSoup(text, 'html.parser')

# for anchor in content.find_all('a'):
#         link = anchor.attrs["href"] if "href" in anchor.attrs else ''
#         # print('link',link)
#         for links in link:
#             res = requests.get(url, headers=headers, timeout=30)
#             text += res.text
#                 # print('text ', text)
#             content = BeautifulSoup(text, 'html.parser')
#             for anchor in content.find_all('a'):
#                 link = anchor.attrs["href"] if "href" in anchor.attrs else ''
#                 print('link',link)
data=crawler(url, out_file='sitemap.xml', exclude_urls=[".pdf", ".jpg", ".zip"])
print('data', data)