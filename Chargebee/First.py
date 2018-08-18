if __name__=='__main__':
    n=input()
    globalDup=[]
    li=map(int, raw_input().split())
    for i in xrange(0,n):
        cD=li[i+1]-li[i]
        count=1
        sL=set()
        sL.add(li[i])
        sL.add(li[i+1])
        for i in xrange(i+2,n):
            if li[i+2]-li[i+1]==cD:
                count=count+1
                sL.add(li[i+2])
            else:
                if(count>=3) and sL not in globalDup:
                    globalDup.append(sL)
                break


