import requests
from bs4 import BeautifulSoup
html = requests.get('https://finance.sina.com.cn/')
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text,'lxml')
#big_title = soup.select('#blk_hdline_01 h3 a')
#small_title = soup.select('#blk_hdline_01 p a')
zhengquan_title = soup.select('.m-p1-mb2-list.m-list-container ul li a')
#for bg in big_title:
	#print('大标题',bg.text)
	#print('链接: ',bg['href'])
#for sm in small_title:
	#print('小标题',sm.text)
	#print('链接: ',sm['href'])
for zq in zhengquan_title:
	print('标题',zq.text)
	print('链接: ',zq['href'])
	innerHtml = requests.get(zq['href'])
	innerHtml.encoding='utf-8'
	soup2 = BeautifulSoup(innerHtml.text,'lxml')
	articles = soup2.select('div.article p')
	str=''
	for article in articles:
		str += article.text
	print(str)

