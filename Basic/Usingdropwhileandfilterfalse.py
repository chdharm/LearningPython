#Using dropwhile and filterfalse
import itertools
li=[2,4,5,7,8]
print "The value after condition return"
print list(itertools.dropwhile(lambda x: x%2==0,li))
print "The value that return false values"
print list(itertools.ifilterfalse(lambda x:x%2==0,li))