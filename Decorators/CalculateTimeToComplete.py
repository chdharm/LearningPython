import time
def time_decorator(func):
    #print func
    def wrapper(*args,**kwargs):
        #print args
        start=time.time()
        #print start
        print kwargs
        print args
        result=func(*args,**kwargs)
        print result
        end=time.time()
        print func.__name__+"took"+str((end-start)*1000)+"milisecond"
        return result
    return wrapper

@time_decorator
def square(num):
    pass

@time_decorator
def cube(num):
    return num*num*num

@time_decorator
def tcube(num):
    return num*num*num
#print square(5)
#print cube(12)
print square(5)
#cube(12)