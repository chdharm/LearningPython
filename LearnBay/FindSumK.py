########################Done####################

#First approach
def getPair(li,sum):
    l=len(li)
    for i in range(l):
        for j in range(l):
            if (li[i]+li[j])==sum:
                return [i,j]
    return [-1,-1]
#Second approach
def getPair2(li,sum):
    #This approach can be sorting ,In this approach we can take a start pointer and a end pointer and then we can traverse using start++ and end--
    #We will check every stage if a[i]+a[j]==sum if exist
    pass
#Third Approach
def getPair3(li,sum):
    #We can use hashtable : suppose we have an array we want it to be in hashtable for getting sum easily , we will first take sum of all
    #values in array and then for each i in array we will search (sum-arr[i]) in hashtable in 0(1). So only we will be charged for one time
    #traversal over array because we can get the hashtable element in 0(1)
    pass

if __name__=='__main__':
    n=input("Enter the size of array")
    li=[]
    for i in range(n):
        li.append(input())
    sum=input()
    #Simplest program
    print getPair(li,sum)

