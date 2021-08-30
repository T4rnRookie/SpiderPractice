from multiprocessing import Process,Queue,set_start_method
import time,random,os

def consumer(q):
	while True:
		res = q.get()
		if res =='Finish':
			print('消费者进程关闭')
			break
		time.sleep(random.randint(1,3))
		print('\033[45m{} 吃{}\033[0m'.format(os.getpid(),res))
def producer(q):
	for i in range(10):
		time.sleep(random.randint(1,3))
		res = '包子{}'.format(i)
		q.put(res)
		print('\033[44m{} 生产了{}\033[0m'.format(os.getpid(),res))
	q.put('Finish')
	q.put('Finish')

if __name__ == '__main__':
	set_start_method('fork')#mac
	q = Queue()
	p1 = Process(target=producer,args=(q,))
	c1 = Process(target=consumer,args=(q,))
	#c2 = Process(target=consumer,args=(q,))
	p1.start()
	c1.start()
	#c2.start()
	print('主')
