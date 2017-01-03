import threading
import time

def run(n):
	print('task:',n)
	time.sleep(2)
	print('task done:',n)
	
startTime = time.time()

t_obj = []

for i in range(10):
	t = threading.Thread(target=run, args=(i,))
	t.start()
	t_obj.append(t)
for i in t_obj:
	i.join()

print('all thread is done')
print('cost:',time.time() - startTime)
#print("hello world")