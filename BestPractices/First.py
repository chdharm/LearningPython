import os
import urllib
u=urllib.urlopen("http://www.google.com")
data=u.read()
print data
dir=os.getcwd()
#os.mkdir(dir+'/temp')
with open(dir+'/tempfile.txt','w') as of:
    of.write("hgfjvmjhgvmjnhvh")
    of.write(data)
    of.close()