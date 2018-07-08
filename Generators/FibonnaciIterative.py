def fib(n):
    if(n<2):
        yield n
    li=[0,1]
    for i in range(2,n+1):
        li.append(li[i-1]+li[i-2])
    re=li[n]
    yield re

my_name=fib(6)
print my_name
for i in my_name:
    print i