from bs4 import BeautifulSoup
import requests

url='https://search.yahoo.com/search;_ylt=AwrgMKVmG_5ixz8JPklXNyoA;_ylc=X1MDMjc2NjY3OQRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkA1dJOU5LN25CUzJHOEpxaFNjYS4wb0EEbl9yc2x0AzAEbl9zdWdnAzEwBG9yaWdpbgNzZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMyNARxdWVyeQNob3clMjB0byUyMG1ha2UlMjBtb25leSUyMG9ubGluZQR0X3N0bXADMTY2MDgyMDg1Nw--?p=how+to+make+money+online&fr2=sb-top&fr=sfp'
text=''
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
res = requests.get(url, headers=headers, timeout=30)
text += res.text
    # print('text ', text)
content = BeautifulSoup(text, 'html.parser')
# print('content',content.text)
textsc=content.find_all('div', attrs={'class':'compContainerExp'})

# print('texts',textsc.text)
for teee in textsc:
        # list.append(teee)
        # return keyword
    print('teee teee',teee.text)