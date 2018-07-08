n=input("Enter the number")
result=0
while n>0:
    result=result+n%10
    n=n/10
print result
