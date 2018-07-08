import os
#os.chdir('C:\Users\Admin\Desktop/')
#path=os.getcwd()
#print path
path='C:/Users/Admin/Desktop/'
#f=open(path/'dummyrecords.txt',"r")
with open(path+'/dummyrecords.txt','r') as of:
    li=of.readline()
    of.close()
#li=f.read()
print li[1  ]


'''   
import os
dir=''
#os.mkdir(dir+'/temp')
with open(dir+'/tempfile.txt','w') as of:
    of.write("hgfjvmjhgvmjnhvh")
    of.write(data)
    of.close()
'''
