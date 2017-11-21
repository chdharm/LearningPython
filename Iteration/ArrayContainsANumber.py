array = raw_input().split()
flag=0
num=int (raw_input('Please enter the number'))
for i in range(0,len(array)):
    array[i]=int(array[i])
    if array[i]== num :
        flag=1
        break
if flag==1 :
    print 'Yes got it'
else:
    print 'We didn\'t get it'


