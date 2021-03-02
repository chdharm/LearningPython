# A semaphore is a variable used to control access to a critical section in a multi-processing environment. In a multi-processing environment (a program that involves more than 1 thread/process), a critical section is a group of resources (variables, data, etc) shared among threads/processes.

"""
Implementation 3: Use Semaphores
"""

import queue
import threading

orders = queue.Queue()
has_order = threading.Semaphore(value=0)  # ADDED THIS


def serving_line_or_consumer():
    while has_order.acquire():  # ADDED THIS: Acquire a Semaphore, or sleep until the counter of semaphore is larger than zero
        new_order = orders.get()
        # prepare meals from `new_order`, assuming GIL is released while preparing meals
        orders.task_done()


def order_line_or_producer():
    # Each staff in the serving line produces 200 orders
    for _ in range(200):
        orders.put("Order")
    has_order.release() # ADDED THIS: Release the Semaphore, increment the internal counter by 1


# Let's put 4 staff into the order line
order_line = [threading.Thread(target=order_line_or_producer) for _ in range(4)]

# Let's assign 6 staff into the serving line
serving_line = [threading.Thread(target=serving_line_or_consumer) for _ in range(6)]

# Put all staff to work
[t.start() for t in order_line]
[t.start() for t in serving_line]


# "join" the order, block until all orders are cleared
orders.join()

# "join" the threads, ending all threads
[t.join() for t in order_line]
[t.join() for t in serving_line]



#Points to consider
# 1:  In case of locks , locks are not shared accross different processes
# 2: A mutex is the same as a lock but it can be system wide(shared by different processes too)
#3: A semaphore does the same as a mutex but allows x number of threads to enter, this can be used for example to limit the number of cpu, io or ram intensive tasks running at the same time.

