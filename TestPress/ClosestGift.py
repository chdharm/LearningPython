import math
def isPrime(num):
    if (num == 2):
        return True
    if num<2 or num%2==0:
        return False
    for i in xrange(3,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def findClosestGift(num):
    small=0
    large=0
    i=0;
    while(1):
        if i<=num and isPrime(i):
            small=i
        if i>num and isPrime(i):
            large=i
            break
        i=i+1
    return [small,large]

if __name__=='__main__':
    a=input()
    print findClosestGift(a)
