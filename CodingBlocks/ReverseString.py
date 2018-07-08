str=input("Enter the string to be ")
li=list(str)
#print li
l=len(li)
#print l
i=0
j=l-1
while i<j:
    li[i],li[j]=li[j],li[i]
    i=i+1
    j=j-1
print "".join(li)
