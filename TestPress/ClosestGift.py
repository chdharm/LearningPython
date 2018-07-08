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
    if num<=2:
        return 2
    if isPrime(num):
        return num
    li=[]
    count=0
    i=2
    while count<num:
        count=count+1
        if isPrime(i):
            li.append(i)
        i=i+1
    for i in range(0,count):



if __name__=='__main__':
    a=input()
    print isPrime(a)
