class Observable(object):
    def __init__(self):
        self.queues = {}

    def addObserver(self, observer):
        if not observer in self.queues:
            self.queues[observer] = Queue()
            ot = ObserverThread(observer, self.queues[observer])
            ot.start()

    def removeObserver(self, observer):
        if observer in self.queues:
            self.queues[observer].put('die')
            del self.queues[observer]

    def notifyObservers(self, state):
        for queue in self.queues.values():
            queue.put(state)

class ObserverThread(Thread):
    def __init__(self, observer, queue):
        self.observer = observer
        self.queue = queue

    def run(self):
        running = True
        while running:
            state = self.queue.get()
            if state == 'die':
                running = False
            else:
                self.observer.stateChanged(state)