from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import html5lib

from lxml import etree

new_urls = deque(['https://vdc.epson.com/'])

processed_urls = set()


url = new_urls.popleft()
processed_urls.add(url)

# extract base url to resolve relative links
parts = urlsplit(url)
base_url = "{0.scheme}://{0.netloc}".format(parts)
path = url[:url.rfind('/')+1] if '/' in parts.path else url

# get url's content
# print("Processing %s" % url)
# try:
response = requests.get(url)
# print('response', response)

soup = BeautifulSoup(response.content, features="lxml")

# soups = BeautifulSoup(response.content)

soups = BeautifulSoup(response.text).text
soupslen= len(soups)
print('soups', soupslen)

# table = soup.find('div', {'id':'root'}) 
# print('table', table)

# anchor =soup.findAll("script")
# print('anchor', anchor)


# print('herf', herf)

for anchors in soup.findAll("script"):
    if 'www.googletagmanager.com' in anchors or 'google-analytics.com':
        # print('googleAnalytics')
        pass

    if 'www.weebly.com' in anchors:
        print('weebly')
    
    if 'prestashop' in anchors:
        print('prestashop')
    
    
for meta in soup.findAll("meta"): 
    metaname = meta.get('name', '').lower() 
    if metaname == 'generator': 

        if "googleAnalytics" in meta.get('content'): 
            print ('googleAnalytics')

        if "WordPress" in meta.get('content'): 
            print ('WordPress') 

        if "Wix.com Website Builder" in meta.get('content'): 
            print ('wixxxxx')

        if "blogger" in meta.get('content') or 'blogspot' in meta.get('content'): 
            print ('blogger')
        
        if "Weebly" in meta.get('content'): 
            print ('Weebly')
        
        if 'Ghost' in meta.get('content'): 
            print('Ghost')

        if 'drupal' in meta.get('content'): 
            print('drupal')
        
        if 'Joomla' in meta.get('content') or 'MYOB' in meta.get('content'): 
            print('Joomla')
        
        if "bigcommerce" in meta.get('content'): 
            print ('Bigcommerce')
        
        if 'squarespace' in meta.get('content'): 
            print('squarespace')
        
        if 'shopify' in meta.get('content'): 
            print('shopifyssss')
    

    if metaname == 'msapplication-config': 
        if "bigcommerce" in meta.get('content'): 
            print ('Bigcommerce')
    
    metanames = meta.get('property', '').lower() 
    if metanames == 'og:image': 

        if 'shopify' in meta.get('content'): 
            print('shopifyssss')

        if 'squarespace' in meta.get('content'): 
            print('squarespace')

        if 'ghost' in meta.get('content'): 
            print('Ghost')
        
        if 'joomla' in meta.get('content'): 
            print('joomla')

for meta in soup.findAll("script"): 
    # print('meta', meta)
    metaname = meta.get('type', '').lower() 
    # print ('>>>',metaname) 
    if metaname == 'text/javascript': 
        # print("True") 
        if 'weebly' in '_W.configDomain': 
            print('weebly')

herf =soup.findAll('a')
if herf:
    herflen= len(herf)
    print('herflen', herflen)

image =soup.findAll("img")
# print('image',image)
if image:
    # print('image', image)
    imagelen= len(image)
    print('imagelen', imagelen)

title= soup.find('title')
if title:
    print('title', title)
# title= len(title)
# print('title', title)

header1= soup.findAll('h1')
if header1:
    print('header1', header1)
    hlength1= len(header1)
    print('hlength1', hlength1)

header2= soup.findAll('h2')
if header2:
    # print('header2', header2)
    hlength2= len(header2)
    print('hlength2', hlength2)

header3= soup.findAll('h3')
if header3:
    print('header3', header3)
    hlength3= len(header3).text
    print('hlength3', hlength3)

header4= soup.findAll('h4')
print('header4', header4)
# hlength4= len(header4)
# print('hlength4', hlength4)

header5= soup.findAll('h5')
if header5:
    print('header5', header5)
    hlength5= len(header5)
    print('hlength5', hlength5)

header6= soup.findAll('h6')
if header6:
    print('header6', header6)
    hlength6= len(header6)
    print('hlength6', hlength6)