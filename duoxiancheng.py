import threading
import time


def example(name):
	print('线程正在运行: ',name)
	time.sleep(1)
	print('线程运行结束:',name)
if __name__ == '__main__':
	t1= threading.Thread(target=example,args=('t1',))
	t2= threading.Thread(target=example,args=('t2',))
	t1.start()
	t2.start()