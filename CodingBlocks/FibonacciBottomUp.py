def fib(n):
    li=[0,1]
    if n<2:
        return li[n]
    for i in range(2,n+1):
        li.append(li[i-1]+li[i-2])
    return li[n]

for _ in range(100):
    print fib(_)