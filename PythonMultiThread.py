#!/usr/bin/env python3

from threading import Thread
import time

start = time.time()

class MyThread(Thread):
    def run(self):
        for _ in range(10):
            print("Child Thread")
            time.sleep(1)

threads = []

for _ in range(10):
    threadObj = MyThread()
    threadObj.start()
    threads.append(threadObj)

for thread in threads:
    thread.join()




end = time.time()
print("\ntime {}".format(end - start))