import requests
import bs4
session = requests.session()
session.cookies.set('JSESSIONID', session.cookies.get('JSESSIONID'))#有cookies校验
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
def getCapatche():
	url='http://jwzx.hrbust.edu.cn/academic/getCaptcha.do'#接口
	r = session.get(url=url,headers=headers)
	with open ('capatche.jpg','wb') as f:
		f.write(r.content)
	return 1
def login():
	capatche=0#初始化
	url2 = 'http://jwzx.hrbust.edu.cn/academic/j_acegi_security_check'
	status=getCapatche()
	if(status!=1):
		return '验证码获取失败'
	else:
		capatche=str(input('请输入验证码: '))
	params={
	"j_username":"username",
	"j_password":"password",
	"j_captcha":capatche
	}
	response = session.post(url=url2,params=params,headers=headers)
	if('综合教务系统' in response.text):
		return '登录成功'
	else:
		return '登录失败'
def guakecheck():
	flag='不及格\n        '
	course =[]
	url3= 'http://jwzx.hrbust.edu.cn/academic/manager/score/studentOwnScore.do?groupId=&moduleId=2020&randomString=202107131238352gbgw'
	params={
		"year":"41",#2021为第四十一年
		"term":"1"#第几学期
	}
	check = login()
	response2= session.post(url=url3,params=params,headers=headers)
	doc = bs4.BeautifulSoup(response2.text, 'html.parser')
	for el in doc.find_all('td'):
		course.append(el.text)
	if(flag in course):
		l = course.index(flag)
		print(''.join(course[l-10:l+1]))
		print('挂科了')
		print('垃圾')
	else:
		print('你没挂科 下学期必挂')

if __name__ == '__main__':
	guakecheck()

    



