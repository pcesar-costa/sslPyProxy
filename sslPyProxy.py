import requests
from bs4 import BeautifulSoup

class Proxy:
    
    def __init__(self, anonymity = 'all', https = False):
        self.proxies = []
        self.anonymity = anonymity
        self.https = https if anonymity != 'all' else False
        
        sess = requests.Session()
        page = sess.request(method='GET', url='https://www.sslproxies.org/')
        soup = BeautifulSoup(page.content, 'html.parser')

        for row in soup.tbody.find_all('tr'):
            _anonymity = row.find_all('td')[4].string
            _https = False if row.find_all('td')[6].string == 'no' else True

            if(self.anonymity == 'all'):
                    self.proxies.append({'ip':row.find_all('td')[0].string, 'port':row.find_all('td')[1].string})

            if(_anonymity == self.anonymity and self.https):
                if(_https):
                    self.proxies.append({'ip':row.find_all('td')[0].string, 'port':row.find_all('td')[1].string})
            elif(_anonymity == self.anonymity):
                self.proxies.append({'ip':row.find_all('td')[0].string, 'port':row.find_all('td')[1].string})
                
    def getProxies(self):
        return self.proxies
