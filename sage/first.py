import math
def is_prime(n):
    if n == 1 or n ==2 or n ==3:
        return True
    if n%2 == 0 or n%3==0:
        return False
    # (6n+1)(6n-1)
    for j in range(1, int(math.sqrt(n))+1, ):
        if n % j == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(1, 101):
        if is_prime(i):
            print(i)
