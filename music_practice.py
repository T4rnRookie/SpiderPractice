import requests
from bs4 import BeautifulSoup
import os,json
import re
#参数太多了不知道什么意思了(没爬成功)

hash_com = re.compile('"Hash":"(.*?)"',re.I|re.S)
headers={
	"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
	'cookie':'kg_mid=ff7ee29a32825529b746acf6320ca028; kg_dfid=2mT7Ym1uep742pbAhT04llTm; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1628823714; kg_mid_temp=ff7ee29a32825529b746acf6320ca028; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1628824562'
}
html = requests.get('https://www.kugou.com/yy/html/rank.html')
hash_result = hash_com.findall(html.text)
print(hash_result)
base_url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19100006128045438271723_1628824495392&hash='
for hash in hash_result:
	url =base_url+hash
	jsondata=requests.get(url,headers=headers)
	print(jsondata.text)
