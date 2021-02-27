import queue
import threading

orders = queue.Queue()


def serving_line_or_consumer():
    has_order = True
    while has_order:
        new_order = orders.get()

        if new_order is None:   # Check for Sentinel Value
            has_order = False
        print("orders: {}".format(orders))
        # prepare meals from `new_order`, assuming GIL is released while preparing meals
        orders.task_done()  # Invoke this to indicate the "order" in the Queue is processed


def order_line_or_producer():
    # Each staff in the serving line produces 200 orders
    for _ in range(200):
        orders.put("Order")


# Let's put 4 staff into the order line
order_line = [threading.Thread(target=order_line_or_producer) for _ in range(4)]

# Let's assign 6 staff into the serving line
serving_line = [threading.Thread(target=serving_line_or_consumer) for _ in range(6)]

# Put all staff to work
[t.start() for t in order_line]
[t.start() for t in serving_line]

# ADDED THIS: Inform serving line no more orders
[orders.put(None) for _ in range(len(serving_line))]

# "join" the order, block until all orders are cleared
orders.join()

# "join" the threads, ending all threads
[t.join() for t in order_line]
[t.join() for t in serving_line]