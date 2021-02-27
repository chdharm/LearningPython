from queue import Queue, Empty
import threading
from time import sleep

started = False
running = True

class producer(threading.Thread):

    def __init__(self, list_of_numbers):
        threading.Thread.__init__(self)
        self.list_items = list_of_numbers

    def run(self):
        started = True
        for i in self.list_items:
            queue.put(str(i))
        running = False

class consumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not started:
            sleep(0)

        while running:
            try:
                queue_ret = queue.get(block=False)
            except Empty:
                sleep(0)
                continue
            print("Retrieved", queue_ret)


queue = Queue()
producers = producer([10,20,5,4,3,2,1])
consumers = consumer()

producers.start()
consumers.start()
producers.join()
consumers.join()