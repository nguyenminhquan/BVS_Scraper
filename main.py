from scraper import Scraper
from queue import Queue
from threading import Thread

FREQUENCY = 1
TAB = 0
UNIT = 1000
FINAL_YEAR = 2016
NUM_WORKER_THREADS = 15
SRC = 'stock_list.txt'

q = Queue()	
with open(SRC, 'r') as f:
	for line in f:
		q.put(line.strip())
	
def create_job():
	worker = Scraper(FREQUENCY,TAB,UNIT,FINAL_YEAR)
	while True:
		item = q.get()
		worker.do_work(item)
		print(item+' is downloaded | '+str(q.qsize())+' item(s) left')
		q.task_done()

#Create jobs
for _ in range(NUM_WORKER_THREADS):
     t = Thread(target=create_job)
     t.daemon = True
     t.start()

q.join()


	
