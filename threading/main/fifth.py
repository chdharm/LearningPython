from queue import Queue

# create queue
q = Queue()

# add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1

# now q looks like this:
# back --> 3 2 1 --> front

# get and remove first element
first = q.get() # --> 1
print(first)
