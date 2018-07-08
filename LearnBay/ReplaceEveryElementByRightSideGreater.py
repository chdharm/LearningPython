#ReplaceEveryElementByRightSideGreater but excluding the number
n=input()
li=[]
for i in range(n):
    li.append(input())
l=len(li)
for i in range(l-1):
    max=li[i+1]
    for j in range(i+2,l):
        if li[j]>max:
            max=li[j]
    li[i]=max
for i in range(n):
    print i