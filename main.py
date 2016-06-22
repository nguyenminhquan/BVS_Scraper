from scraper import Scraper
from queue import Queue
from threading import Thread
from general import *
import os

# Load stock list into the queue
try:
    q = Queue()
    with open('stock_list.txt', 'r') as f:
        for line in f:
            q.put(line.strip())
except FileNotFoundError:
    print('"stock_list.txt" is missing!')
    raise SystemExit

# Gets the arguments from the command line
args = get_arguments()

FREQUENCY = args.frequency
TAB = args.tab
UNIT = args.unit
FINAL_YEAR = args.final_year
PATH = args.path
NUM_WORKER_THREADS = 15

# Create data folder
make_directory(PATH)


def create_job():
    worker = Scraper(FREQUENCY, TAB, UNIT, FINAL_YEAR)
    while True:
        item = q.get()
        worker.do_work(item)
        print(item + ' is downloaded | ' + str(q.qsize()) + ' item(s) left')
        q.task_done()

# Create jobs
for _ in range(NUM_WORKER_THREADS):
    t = Thread(target=create_job)
    t.daemon = True
    t.start()

q.join()
