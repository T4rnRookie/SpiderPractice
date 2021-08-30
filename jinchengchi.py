from multiprocessing import Pool
import os,time

def work(n):
	print('%s run'%os.getpid())
	time.sleep(3)
	return n**2
if __name__ == '__main__':
	p = Pool(3)
	res_l = []
	for i in range(10):
		res = p.apply_async(work,args=(i,))
		res_l.append(res)
	p.close()
	p.join()
	for res in res_l:
		print(res.get())