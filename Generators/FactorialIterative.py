def factorial(num):
    if num<2:
        yield 1
    fact=1
    for i in range(1,num+1):
        fact=fact*num
    yield fact

def factorial2(num):
    if num<2:
        return num
    return num*factorial2(num-1)


my_name=factorial(4)
print my_name
for i in my_name:
    print i