def RequiredMove(li, start, last):
    countO = 0
    countC = 0
    for i in xrange(start, last):
        if li[i]%2==0: countO = countO + 1
        else: countC = countC + 1
    if countO >= countC:
        return 0
    else:
        diff =countC-countO
        return diff/2 if diff%2==0 else diff/2+1


if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        a = input()
        li = map(int, raw_input().split())
        Nq = input()
        for i in xrange(Nq):
            start,last = map(int, raw_input().split())
            print RequiredMove(li, start-1, last)