import requests
import random
from bs4 import BeautifulSoup

class Proxy:
    
    def __init__(self, anonymity = 'all', https = False, region = []):
        self.proxies = {}
        self.anonymity = anonymity
        self.https = https if anonymity != 'all' else False
        self.region = region
        
        sess = requests.Session()
        page = sess.request(method='GET', url='https://www.sslproxies.org/')
        soup = BeautifulSoup(page.content, 'html.parser')

        for row in soup.tbody.find_all('tr'):
            _anonymity = row.find_all('td')[4].string
            _https = False if row.find_all('td')[6].string == 'no' else True
            _ip = row.find_all('td')[0].string
            _port = row.find_all('td')[1].string
            _code = row.find_all('td')[2].string

            hashKey = hex(hash((random.random() ** 3) * random.random()))

            if(self.anonymity == 'all'):
                self.proxies.update({hashKey: [_ip+':'+_port, _code]})
            else:
                if(_anonymity == self.anonymity and self.https):
                    if(_https):
                        self.proxies.update({hashKey: [_ip+':'+_port, _code]})
                elif(_anonymity == self.anonymity):
                    self.proxies.update({hashKey: [_ip+':'+_port, _code]})

    def getProxies(self):
        return self.proxies

    def randomProxy(self):
        self.randomKey = random.sample(self.proxies.keys(), 1)[0]
        return self.proxies[self.randomKey][0]

    def setRegion(self, regionList):
        self.region = regionList
        data = self.proxies.copy()
        for key, code in data.items():
            try:
                if (code[1] not in regionList):
                    del self.proxies[key]
            except:
                continue

    def removeRandom(self):
        try:
            del self.proxies[self.randomKey]
            self.randomKey = ''
        except:
            return

    def removeByKey(self, keyProxy):
        del self.proxies[keyProxy]
