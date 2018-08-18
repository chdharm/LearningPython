def compare(a,b):
    if int(a+b)>int(b+a):
        return True
    else:
        return False

if __name__=='__main__':
    str=raw_input()
    li=str.split()
    l=len(li)
    print li
    for i in range(l-1):
        max=i+1
        for j in range(i+1,l):
            if compare(li[j],li[max]):
                max=j
        if compare(li[max],li[i]):
            li[max],li[i]=li[i],li[max]
    print ''.join(li)