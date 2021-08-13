from lxml import etree
import requests
#url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
url ='https://book.douban.com/latest?icn=index-latestbook-all'
headers={
	"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
html = requests.get(url=url,headers=headers)
soup = etree.HTML(html.text)
#result = soup.xpath("//a/font/b/text()")
#result = soup.xpath("//li[contains(@class,'subject')]/div/a/img/@src")
result = soup.xpath("//li/a[contains(@class,'cover')]/img/@src")
for i in result:
		print(i)