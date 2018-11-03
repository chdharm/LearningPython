if __name__=='__main__':
    t=input()
    for i in range(t):#Number of Test cases
        n=input()
        d={}
        for j in range(n):#Number of tweets
            name=raw_input().split()[0]
            if name in d.keys():
                d[name]+=1
            else:
                d[name]=1
