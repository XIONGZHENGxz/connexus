import Queue
from datetime import *
def testq(queue):
	new_queue=Queue.Queue()
	for item in queue.queue:
		new_queue.put(item)	
	new_queue.get()
	return new_queue

if __name__=="__main__":
	queue=Queue.Queue()
	queue.put(4)
	queue.put(5,6)
	q=testq(queue)
	btime=datetime(2016,1,1,1)
	now=datetime.now()
	dtime=(datetime.now()-datetime(2016,1,1,1)).total_seconds()
	print dtime
	time=timedelta(hours=1)
	time =datetime.now()
	print time.second

