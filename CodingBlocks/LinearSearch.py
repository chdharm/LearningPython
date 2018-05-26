t=input("Enter the number of elements:")
li=[]
while t:
    li.append(input("Enter list element"))
    t=t-1
find=0
target=input("Enter the element to search")
for _ in li:
    if _==target:
        print "Number is at %s index"%li.index(_)
        find=1
        break
if find==0:
    print "can't find the number"