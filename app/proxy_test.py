import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import random
import json

https_p = ['185.117.118.3:5836', '188.170.233.102:3128', '195.22.148.8:5836',
'88.170.233.107:3128', '188.170.233.113:3128', '89.108.112.1:8013', 
'195.22.148.4:5836']


def yandex_parser(m_class):
    global https_p
    res = []
    _https = https_p.copy()
    urls = set()
    flag = True
    for i in range(len(_https)):
        try:
            htps = random.choice(_https)
            print(htps)
            _https.remove(htps)
            proxies = {
            'https': "https://" + htps}       
            url = "https://yandex.ru/images/search?text=" + str(m_class) + i
            page = requests.get(url, headers=Headers().generate(), proxies=proxies)
            soup = BeautifulSoup(page.text, "html.parser")
                
            result = soup.find_all("div", {"class":"serp-item"}, limit=50)
            for r in result:
                if count >3:
                    return list(urls)
                jsonify = json.loads(r["data-bem"])
                urls.add(jsonify['serp-item']['preview'][0]['url'])
                if len(urls)>=1:
                    res.append(htps)
                    count+=1
                    continue
                else:
                    continue
            return 
        except:
            pass
    return res

y = yandex_parser('cat')
print(y)