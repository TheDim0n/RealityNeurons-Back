import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import random
import json


https_p = [ '109.174.19.134:80', '109.174.19.134:8385', '31.28.99.25:31396',
'85.26.146.169:80', '85.175.99.136:8080', '46.20.74.109:3128',
'79.171.13.166:33117', '84.52.76.91:41258', '91.77.162.117:8080', '87.249.22.114:8080',
'195.22.148.4:5836']


def yandex_parser(m_class):
    global https_p
    _https = https_p.copy()
    help = ["", " page 0", " page 1", " page 2"]
    urls = set()
    flag = True
    while(flag):
        try:
            htps = random.choice(_https)
            print(htps)
            _https.remove(htps)
            proxies = {
            'https': "https://" + htps
    }       
            count = 0
            for i in help:
                url = "https://yandex.ru/images/search?text=" + str(m_class) + i
                page = requests.get(url, headers=Headers().generate(), proxies=proxies)
                soup = BeautifulSoup(page.text, "html.parser")
                print('here')
                result = soup.find_all("div", {"class":"serp-item"}, limit=50)
                for r in result:
                    jsonify = json.loads(r["data-bem"])
                    urls.add(jsonify['serp-item']['preview'][0]['url'])
                    print(len(urls))
                    if count > 20:
                        return list(urls)
                    count+=1
                if len(urls)>=1:
                    flag = False
                else:
                    continue
            urls = list(urls)
        except:
            pass
    return urls
