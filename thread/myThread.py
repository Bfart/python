import threading
from time import ctime

class myThread(threading.Thread):
	def __init__(self,func,args,name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args
		self.res = ''
		
	def getResult(self):
		return self.res
		
	def run(self):
		print('starting %s at:%s'% (self.name,ctime()))
		#self.res = apply(self.func, self.args) 3.2以上已经不支持这个函数了 改为self.func(*self.args)
		self.res = self.func(*self.args)
		print('%s finished at:%s'% (self.name,ctime()))