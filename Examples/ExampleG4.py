import sys
num=input("Enter the number:")
print type(num)
#print num
print "size:===",sys.getsizeof(num)
for i in num:
    print i
#l=num.split(",")
#print type(l)
#print l