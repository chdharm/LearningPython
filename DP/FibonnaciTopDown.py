def fib(n):
    if n<2:
        return n
    elif table[n]==-1 :
        table[n]=fib(n-1)+fib(n-2)
        return table[n]
    else:
        result=table[n]
    return result

n=input()
table=[-1 for _ in range(n+1)]
table[0]=0
table[1]=1
print fib(n)