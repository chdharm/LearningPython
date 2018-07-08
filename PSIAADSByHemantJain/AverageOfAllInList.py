class Average:
    @classmethod
    def calAvg(cls,li,be,en):
        if be==en:
            return li[be]
        return li[be]+cls.calAvg(li,be+1,en)
li=[]
n=input("Enter the number of elements")
print n
for i in range(n):
    li.append(input())
print Average.calAvg(li,0,len(li)-1)
# print li


