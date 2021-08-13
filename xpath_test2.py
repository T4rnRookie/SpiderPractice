from lxml import etree
import requests
url ='https://book.douban.com/top250?icn=index-book250-all'
url2 = 'https://book.douban.com/top250?start=25'
headers={
	"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
html = requests.get(url=url,headers=headers)
html2 = requests.get(url=url2,headers=headers)
#print(html.text)
soup = etree.HTML(html.text)
soup2 = etree.HTML(html2.text)
#result = soup.xpath("//a/font/b/text()")
#result = soup.xpath("//li[contains(@class,'subject')]/div/a/img/@src")
#result = soup.xpath("//li/a[contains(@class,'cover')]/img/@src")
#result = soup.xpath("//th[contains(@class,'common')]/a[contains(@class,'s xst')]/text()")
#result = soup.xpath("//th[contains(@class,'common')]/img/@src")
result = soup.xpath("//tr[contains(@class,'item')]/td[contains(@valign,'top')]/div[contains(@class,'pl2')]/a/@title")
result2 = soup2.xpath("//tr[contains(@class,'item')]/td[contains(@valign,'top')]/div[contains(@class,'pl2')]/a/@title")
for i in result:
	print(i)
for i in result2:
	print(i)
