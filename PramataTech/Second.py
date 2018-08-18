if __name__=='__main__':
    n=input()
    dict1={}
    for i in xrange(n):
        data=raw_input().split()
        k=data[0]
        v=int(data[1])
        if k in dict1.keys():
            dict1[k][0]= dict1[k][0]+1
            dict1[k][1] = dict1[k][1]+ v
        else:
            dict1[k]=[1,v]
    resdict={}
    l=len(dict1)
    for i in xrange(l-1):
        max=dict1[i]
        for i in xrange(i+1,l):
            if dict1[i+1][0]>max[0]:
                max=dict1[i+1]
            elif dict1[i+1][0]==max[0] and dict1[i+1][1]<max[1]:
                max=dict1[i+1]
            elif dict1[i + 1][0] == max[0] and dict1[i + 1][1] == max[1] and dict1[i+1]

