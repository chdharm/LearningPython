# https://melvinkoh.me/solving-producerconsumer-problem-of-concurrent-programming-in-python-ck3bqyj1j00i8o4s1cqu9mfi7
import queue
import threading

orders = queue.Queue()


def serving_line_or_consumer():
    while True:
        new_order = orders.get()
        # orders.task_done()
        # Make the task done
        print("Doing Task | new_order - {}".format(new_order))


def order_line_or_producer():
    for i in range(200):
        orders.put(i)


if __name__ == '__main__':
    print("Log-1")
    order_line = [threading.Thread(target=order_line_or_producer)]
    service_line = [threading.Thread(target=serving_line_or_consumer)]
    print("Log-2")
    [t.start() for t in order_line]
    [t.start() for t in service_line]
    print("Log-3")
    # orders.join()
    print("Log-4")
    [t.join() for t in order_line]
    [t.join() for t in service_line]
    print("Log-5")
