from bs4 import BeautifulSoup
import requests

url='https://www.runwayincubator.com/'
text=''
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
res = requests.get(url, headers=headers, timeout=30)
text += res.text
    # print('text ', text)
content = BeautifulSoup(text, 'html.parser')
print('content',content)

textsc=content.select('a')
for texts in textsc:
    print('texts',texts)

# href=textsc['href']
# href = textsc.split(':')
# print('href',href)
# for i in textsc:
#     href=i['href']
#     try:
#         str1, str2 = href.split(':')
#         print('kjjjk',href.split(':'))
#     except ValueError:
#         break
    
    # emailList.append(str2)

# for teee in textsc:
#         # list.append(teee)
#         # return keyword
#     print('teee teee',teee.text)