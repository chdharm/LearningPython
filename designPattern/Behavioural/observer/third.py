def observe(f):
    def decorated(self,*args,**kwargs):
        for obs in self.observes:
            obs.notify('event',*args,**kwargs)
        return f(self,*args,**kwargs)
    return decorated

class Target(object):
    def __init__(self,*observers):
        self.observes = observers

    @observe
    def otherevent(self,data):
        print "other event with",data