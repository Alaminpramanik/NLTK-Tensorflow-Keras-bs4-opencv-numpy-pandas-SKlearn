import requests


# page = requests.get("http://www.google.com:80", proxies={"http": "http://111.233.225.166:1234"})
aa=requests.get("https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/dp/B0773ZY26F/ref=sr_1_2?crid=1861TM8A5NDPX&dchild=1&keywords=monitors&qid=1597071906&sprefix=monitors%2Caps%2C364&sr=8-2:80", proxies={"http:":"//111.233.225.166:1234"})
print('aaaa',aa)