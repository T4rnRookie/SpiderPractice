#延迟访问
import requests
from urllib.parse import urlparse
from datetime import datetime
import time 
import requests

class Delay:
	def __init__(self,delay=3):
		self.delay = delay
		self.urls={}
	def wait(self,url):
		netloc = urlparse(url)
		#netloc = urlparse(url).netloc
		print(netloc)
		lastOne=self.urls.get(netloc,False)
		if lastOne and self.delay>0:
			sleepTime = self.delay-(datetime.now()-lastOne).seconds
			if sleepTime>0:
				time.sleep(sleepTime)
		self.urls[netloc] = datetime.now()
if __name__ == '__main__':
	urls = ['https://hackerpoet.com/']*10
	d = Delay()
	a
	for url in urls:
		html = requests.get(url)
		d.wait(url)
		print(html.status_code)