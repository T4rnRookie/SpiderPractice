import requests
import os
from bs4 import BeautifulSoup
headers={
	"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
for i in range(1,3):
	print('正在下载第{}页'.format(str(i)))
	html = requests.get('https://588ku.com/sucai/0-default-0-78-0-0-{}/'.format(i),headers=headers)
	soup =BeautifulSoup(html.text,'lxml')
	imgurl = soup.select('div.fl.marony-item div a')
	for iu in imgurl:
		if 'vip' in iu['href']:
			continue
		print('https:'+iu['href'])
		imgData = requests.get('https:'+iu['href'],headers=headers)
		imgsoup =BeautifulSoup(imgData.text,'lxml')
		img = imgsoup.select_one('.img-box img')
		title=img['alt']
		print('无水印','https:'+img['src'])

		if not os.path.exists('qt'):
			os.mkdir('qt')
		with open('qt/{}.jpg'.format(title),'wb') as f:
			f.write(requests.get('https:'+img['src'],headers=headers).content)
			print('图片正在下载...')