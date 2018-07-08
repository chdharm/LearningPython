#First approach
def getPair(li,sum):
    l=len(li)
    for i in range(l):
        for j in range(l):
            if (li[i]+li[j])==sum:
                return [i,j]
    return [-1,-1]
#Second approach
def getPair2():
    #This approach can be sorting ,In this approach we can take a start pointer and a end pointer and then we can traverse using start++ and end--
    #We will check every stage if a[i]+a[j]==sum if exist
    pass
if __name__=='__main__':
    n=input("Enter the size of array")
    li=[]
    for i in range(n):
        li.append(input())
    sum=input()
    #Simplest program
    print getPair(li,sum)

