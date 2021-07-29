import requests

url = 'https://hackerpoet.com'

r = requests.get(url)

print(r.text)