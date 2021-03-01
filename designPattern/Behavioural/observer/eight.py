from abc import ABCMeta, abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

from threading import Thread

class myObserver(Observer):

    def update(self, *args, **kwargs):
        '''update is called in the source thread context'''
        Thread(target=self.handler, args=(self,*args), kwargs=**kwargs).start()

    def handler(self, *args, **kwargs):
       '''handler runs in an independent thread context'''
       pass # do something useful with the args