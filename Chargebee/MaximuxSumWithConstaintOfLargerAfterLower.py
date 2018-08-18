if __name__=="__main__":
    arr=map(int ,raw_input().split())
    l=len(arr)
    max=0
    firstIn=0
    lastIn=0
    for i in range(0,l-1):
        for j in range(i+1,l):
            print "Checking i=",i,"(",arr[i],")","and j=",j,"(",arr[j],") and current max=",max
            if arr[i]<arr[j] and (arr[j]-arr[i])>max:
                max=(arr[j]-arr[i])
                firstIn=i
                lastIn=j
    print max,"i=",i,"j=",j