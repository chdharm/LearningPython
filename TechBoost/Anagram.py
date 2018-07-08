n=input()
cd={}
total=0
for i in range(0,n):
    str=raw_input()
    if len(str)%2!=0:
        print '-1'
        continue;
    mid=len(str)/2;
    cou=0;
    for j in str:
        if cou<mid:
            if(cd.has_key(j)):
                cd[j] =cd[j]+1
            else:
                cd[j]=1
            cou=cou+1
        else:
            if (cd.has_key(j)):
                cd[j]=cd[j]-1
    for i in dict.keys():
        if cd[i]>0:
            total=total+cd[i]
    print total
