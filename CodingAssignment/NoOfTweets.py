if __name__=='__main__':
    t=input()
    while t:
        t-=1
        dic={}
        nt=input()
        while nt:
            nt-=1
            pt=raw_input()
            name=pt.split()[0]
            if name in dic.keys():
                dic[name]+=1
            else:
                dic[name]=1
        max=0
        all_keys=dic.keys()
        for i in all_keys:
            if max<dic[i]:
                max=dic[i]
        li=[]
        for i in all_keys:
            if max==dic[i]:
                li.append(i)
        li.sort()
        for i in li:
            print i ,dic[i]