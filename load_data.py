import os, math
import multiprocessing, threading
import re
import requests
n_thread = 32
def load_data(i):
    with open("multi/GOOD_DATA_%d.txt"%(i),"r") as ids:
        lines = ids.readlines()
        for id in lines:
            if len(id) > 1:
                id = id.strip('\n')
                pid = id.split('/')
                eid = pid[-1]
                os.system('rdsamp -r mimic3wdb/%s -p -v -c >> data/%s.csv'%(id, eid))
                print('finish %s.csv'%(eid))
record = []
lock  = threading.Lock()
for i in range(n_thread):
    thread = threading.Thread(target=load_data,args=(i,))
    thread.start()
    record.append(thread)

for thread in record:
    thread.join()
