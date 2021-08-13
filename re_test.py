import re
import requests
url ='https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
headers={
	"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}
trash = ['<span style="font-size:12px;"> :','</span>']
html =requests.get(url=url,headers=headers)
#print(html.text)
titles = re.compile('<a href="https://.*?" title=.*?>(.*?)</a>',re.I|re.S)
result = titles.findall(html.text)
for r in result[:-1]:
	for t in trash:
		if t in r:
			r=r.replace(t,'')
	print(r.strip().replace('\n','').replace(' ',''))