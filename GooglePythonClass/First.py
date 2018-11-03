

if __name__=='__main__':
    x={}
    print type(x)
    x={'z':1,"y":3}
    print x
    print x.values()
    print sorted(x)
    for i in x.keys():
        print 'value of',i ,'=',x[i]
    for i,j in x.items():
        print i,j
