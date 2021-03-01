import threading

class Observable(object):

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
             del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
        thread = threading.Timer(4,self.update_observers).start()

from abc import ABCMeta, abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

class myObserver(Observer):
    def update(self, *args, **kwargs):
        '''update is called in the source thread context'''
        print(str(threading.current_thread()))

observable = Observable()

observer = myObserver()
observable.register(observer)

observable.update_observers('Market Rally', something='Hello World')