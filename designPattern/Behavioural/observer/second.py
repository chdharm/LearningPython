class Observer(object):
    def notify(self,*args,**kwargs):
        print args,kwargs

class Target(object):
    def __init__(self,*observers):
        self.observes = observers

    #this notify for every access to the function
    def event(self,data):
        for obs in self.observes:
            obs.notify('event',data)
        print "event with",data

t = Target(Observer())
t.event(1)
#('event', 1) {}
#event with 1