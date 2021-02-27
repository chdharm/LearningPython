from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i + 1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()

    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')

import threading
import random, time


def runner(secs):
    print
    threading.current_thread(), 'begin sleep(', secs, ')'
    time.sleep(secs)
    print
    threading.current_thread(), 'end sleep(', secs, ')'


threads = []
for x in xrange(0, 5):
    t = threading.Thread(target=runner, args=(random.randint(1, 10),))
    threads.append(t)
    t.start()

print
'joining ..'
while threading.active_count() > 1:
    for t in threads:
        t.join()
        print
        t, 'is done.'
print
'all done.'

import threading
import random, time


class MyTask(threading.Thread):
    def __init__(self, sleepFor):
        self.secs = sleepFor
        threading.Thread.__init__(self)

    def run(self):
        print
        self, 'begin sleep(', self.secs, ')'
        time.sleep(self.secs)
        print
        self, 'end sleep(', self.secs, ')'


And
here is the
usage
of
the


class defined above.


1
2
3
4
5
6
7
8
9
10
11
12
tasks = []
for x in xrange(0, 5):
    t = MyTask(random.randint(1, 10))
    tasks.append(t)
    t.start()

print
'joining ..'
while threading.active_count() > 1:
    for t in tasks:
        t.join()
        print
        t, 'is done.'
print
'all done.'

import threading
import random, time

threads = []
for x in xrange(0, 5):
    t = threading.Thread(target=lambda x: time.sleep(x), args=(random.randint(1, 10),))
    threads.append(t)
    t.start()

print
'joining ..'
while threading.active_count() > 1:
    for t in threads:
        t.join()
        print
        t, 'is done.'
print
'all done.'

import threading


def runner(ev):
    print
    threading.current_thread(), 'started.'
    while not ev.is_set():
        ev.wait(0.5)
    print
    threading.current_thread(), 'completed.'

threads = []
ev = threading.Event()
for x in xrange(0, 5):
    t = threading.Thread(target=runner, args=(ev,))
    threads.append(t)
    t.start()





