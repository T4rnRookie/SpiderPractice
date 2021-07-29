import requests

url = 'https://www.baidu.com/1&a=-1'
url = url.split('/')
#print(url)
url = '/'.join(url[:3])
#print(url)
ends = 'robots.txt'
url = url+'/'+ends
r = requests.get(url)
print(r.text)