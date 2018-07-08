li=[0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0]
print li
l=len(li)-1
i=0
#print range(l+11)
while i<l:
    if li[i]==1 and li[l]==0:
        li[i],li[l]=li[l],li[i]
        i=i+1
        l=l-1
        continue;
    if li[i]==1:
        l=l-1
        continue
    if li[l]==0:
        i=i+1
print li