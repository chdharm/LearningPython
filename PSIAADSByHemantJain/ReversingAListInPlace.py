li=[43,65,42,65,4242,9999,53,53,25,2,5,2,90090,525,525552,25,5,5,25,2,5]
print li
l=len(li)-1
i=0
while i<l:
    print "Swaping",li[i],"--and--",li[l]
    li[i],li[l]=li[l],li[i]
    i=i+1
    l=l-1
print "Sorted: ",li