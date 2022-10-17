from bs4 import BeautifulSoup
from urlquote import quote
import re

# text = '<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FDoctorTaniya%2Fposts%2F1906676949620646&width=500" width="500" height="482" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true"></iframe>'
# soup = BeautifulSoup(text)

# src_attribute = soup.find("iframe")["src"]
text='https://instagram.fdac116-1.fna.fbcdn.net/v/t51.2885-19/279453980_339252858189734_6129611620031941134_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdac116-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=XXSWAODnVeMAX_YXIzb&tn=A1HM-1wEyW0bVnKw&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AT8Q-aWGs6A4aWGeFSdemTbK9HE0Lz5LnFvxxes8I8dn2Q&oe=63390265&_nc_sid=a9513d'
# Regex
link = re.findall('.*?href=(.*)?&', text)
# .split()
# link = src_attribute.split("href=")[1].split("&")[0]
print('link',link)
# link = urllib3.unquote(link)
quoted = quote(text)
print('ddd',quoted)
# assert(quoted == '/El%20Ni%C3%B1o/'.encode('utf-8'))