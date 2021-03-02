#!/usr/bin/env python3

import multiprocessing
import time

start = time.time()

def sleep_time():
    print("___ Sleepy time ___")
    time.sleep(1)
    print("___ Done Sleeping ___")

processes = []

for _ in range(10):
    p = multiprocessing.Process(target=sleep_time)
    p.start()
    processes.append(p)

for process in processes:
    process.join()



finish = time.time()

print(f"time : {finish - start}")