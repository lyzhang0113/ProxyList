import json
import pickle
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
url = 'https://www.free-proxy-list.net/'
soup = BeautifulSoup(requests.get(url, headers = headers).text,'lxml')
ips = soup.find_all('tr')
fp = open('host.txt','w')

for i in ips:
    try:
        ipp = i.select('td')
        ip = ipp[0].text
        host = ipp[1].text
        fp.write(ip + '\t' + host + '\n')
    except Exception as e :
        print ('no ip!')
fp.close()

# check proxy
request_url = 'http://www.baidu.com'
fpw = open('working.txt', 'w')
fp = open('host.txt','r')
ips = fp.readlines()
proxys = list()
working = list()
for p in ips:
    ip =p.strip('\n').split('\t')
    address = "http://" +  ip[0] + ':' + ip[1]
    proxy = {"http":address}
    proxys.append(proxy)
i = 1
for pro in proxys:
    if i > 300:
        break
    print(str(i) + '/' + str(len(proxys)) + '\t' + str(pro))
    i += 1
    try :
        s = requests.get(request_url, proxies = pro, timeout=0.5)
        print ('success')
        working.append(pro)
    except Exception as e:
        print ('fail')
print(str(len(working)) + ' working proxies out of ' + str(len(proxys)) + '!')
with open('working.txt', 'wb') as fildhandle:
    pickle.dump(working, fildhandle)