def isTrue(i):
    while i>0:
        if i % 10 != 2 and i % 10 != 5:
            return False
        i=i/10
    return True
n = input()
for i in range(1,n+1):
    if isTrue(i):
        print i
