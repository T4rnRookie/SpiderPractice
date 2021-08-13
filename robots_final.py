import requests
class Robots:
	"""docstring for Robots"""
	def __init__(self,url,Agent):
		self.url =url
		self.headers = {'user-agent':Agent}
	def getRobots(self):
		html = requests.get(self.url)
		with open('robots.txt','r',encoding='utf-8')as f:
			lines = f.readlines()
			flag = False
			domain=[]
			for line in lines:
				#print(line)
				line = line.strip().replace("\n","")
				if(self.headers['user-agent'] in line):
					flag = True
					continue
				elif(line.startswith('Disallow')):
					if flag is True:
						domain.append(line)
				elif line is None or line =='':
					if flag is True:
						break
		return domain
if __name__ == '__main__':
	url = 'https://www.baidu.com/'
	agent = 'Googlebot'
	r = Robots(url,agent)
	print(r.getRobots())
	for d in r.getRobots():
		if d in url:
			print('禁止')
		else:
			print('可以')