if __name__ == '__main__':
    t = input()
    for i in range(t):
        a,b=raw_input().split()
        f=int(a)
        s=int(b)
        try:
            print f / s
        except Error as e:
            print "Error Code:", e
