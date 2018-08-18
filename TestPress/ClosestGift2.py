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
def nearest_prime(n):
    incr = -1
    multiplier = -1
    count = 1
    while True:
        if isPrime(n):
            return n
        else :
            n = n + incr
            multiplier = multiplier * -1
            count = count + 1
            incr = multiplier * count

if __name__=='__main__':
    print nearest_prime(5)