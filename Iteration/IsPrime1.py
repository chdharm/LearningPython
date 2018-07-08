def IsPrime(n):
    import math
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(math.sqrt(n)),2):
            if n%i==0:
                return False
        return True

if __name__ == '__main__':
    n=input("Enter thenumber which you want o check:")
    print IsPrime(n)


