n=input("Enter the size of list")
li=[]
for i in range(n):
    li.append(input())
l=len(li)

# for i in li:
#     print li.indexof(i)
for i in li:
    index=li.index(i)
    if(index==0):
        print i,
    if index==l-1:
        print i,
    if i>li[index-1] and i>li[index+1]:
        print i,