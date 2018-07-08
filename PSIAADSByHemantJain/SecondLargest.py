li=[87,98,56,2323,12,23,67.0908]
max1=-1
max2=0
for i in li:
    print i
    if i>max1:
        max2=max1
        max1=i
    if i>max2 and i!=max1:
        max2=i

print max2