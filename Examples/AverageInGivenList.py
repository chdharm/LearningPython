n=input("Enter the number of elements in given list:")
arr=[]

#Here we are using long procedure

for i in xrange(0,n):
    arr.append(input("Enter the array elements :"))
sum=0
for i in xrange(0,n):
    sum=sum+arr[i]
avg=sum/n
print avg