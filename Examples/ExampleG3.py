'''
n=input("Enter the number: ")
dict={}
dict2={}
for i in range(1,n+1):
    dict[i]=i*i
    dict2.update({i:i*i})
print dict
print dict2
'''
print "-----------------Staring completely new session-----------------"
#Creating a empty dictionary
data1={}
data2={}
data3={}
data4={}
data5={}
#Creating a dictionary with initial values
data1={'a':1,'b':2,'c':3}
print "Printing data 1========================",data1
data2=dict(a=1,b=2,c=3)
print "Printing data 1========================",data2
data3={k:v for k,v in (('a',1),('b',2),('c',3))}
print "Printing data 1========================",data3
#Inserting/Updating a single value
data1['a']=1
data1.update({'a':1})
data1.update(dict(a=1))
data1.update(a=1)
#Inserting/Updating multiple values
data1.update