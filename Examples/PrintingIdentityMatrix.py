n=input("Enter the size of matrix")
for i in range(0,n):
    for j in range(0, n):
        if i==j:
            print "1 ",
        else:
            print "0 ",
    print