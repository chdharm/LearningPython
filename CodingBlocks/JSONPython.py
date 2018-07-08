import json
#In Python 2.5 , we were using simplejson module but in Python 2.7 we are using json module
data={
    "first":"Dharmpal",
    "second":"Chaudhary",
    "rollno":148604
}
print data
#json.dump(data)
vari=json.dumps(data)
print type(vari)
print vari
data=json.loads(vari)
print type(data)
print data
#
# import requests
# req = requests.request('GET', 'http://httpbin.org/get')
# print req

import urllib
urllib.urlopen("http://www.gooogle.com")