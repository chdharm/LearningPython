import math
def checkPrime(n):
    if n<2:
        return False
    if n==2:
        return False
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
n=input("Enter the number:")
for i in range(1,n+1):
    if  n%i==0:
        if checkPrime(i) :
            print i,"It's Prime number"
        else:
            print i,"It's  not Prime number"