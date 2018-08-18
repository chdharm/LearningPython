if __name__=='__main__':
    li=[]
    max=0
    n,k=map(int,raw_input().split())
    li=map(int,raw_input().split())
    for i in xrange(k-1):
        a=li.pop()
        #if a>max:
        max=a
    if li[len(li)-1]>max:
        if li[len(li)-2]>li[len(li)-1]:
            li.pop()
        else:
            pass
    else:
        li.append(max)
    print li.pop()





