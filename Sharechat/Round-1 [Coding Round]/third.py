import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(1, math.sqrt(n), 6):
        if n % (6 * i + 1) == 0 or n % (6 * i - 1):
            return True

    return False


if __name__ == '__main__':
    t = int(input())
    prime_list = []
    prime_list.append(2)
    for i in range(3, 1000000, 2):
        if is_prime(i):
            prime_list.append(i)
    while (t != 0):
        x, y, m = list(map(int, input().split(" ")))
        floor = math.gcd(x, y)
        x_factor = int(x / floor)
        y_factor = int(y / floor)
        time = 0
        for i in range(0, m):
            prime_number = prime_list[i]
            if prime_number >= m:
                break
            while x_factor % prime_number == 0:
                x_factor = int(x_factor / prime_number)
                time += 1
            while y_factor % prime_number == 0:
                y_factor = int(y_factor / prime_number)
                time += 1
            if x_factor == 1 and y_factor == 1:
                break
        if x_factor == 1 and y_factor == 1:
            print(str(time) + " " + str(floor))
        else:
            print("-1")
        t -= 1
