import requests
import json
from pprint import pprint
import polyline
r=requests.get("https://www.google.com/maps/search/real+estate+agents+bangladesh/@23.7745358,90.3671899,13z")

txt = r.text

find1 = "window.APP_INITIALIZATION_STATE="
find2 = ";window.APP"

i1 = txt.find(find1)
i2 = txt.find(find2, i1+1 )
js = txt[i1+len(find1):i2]
data = json.loads(js)
gg=polyline.decode(js)
pprint(data)

