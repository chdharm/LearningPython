import json
dictdp ={
    1:"one",
    2:"two",
    3:"three"
    }



def processJson(dictdp):
     if type(dictdp)==int:
         return str(dictdp)
     elif type(dictdp)==str or type(dictdp)==unicode:
         return '"'+dictdp+'"'
     elif type(dictdp)==list:
         items=[]
         for i in dictdp:
             items.append(processJson(i))
         return "["+",".join(items)+"]"
     elif type(dictdp)==dict:
         return {

             "{"+ +"}"
         }




'''
def processJson(dictdp):
    if type(dictdp)!='dict':
        print type(dictdp)
        return
    print '{'
    for i in xrange(1, len(dictdp.keys()) + 1):
        processJson(dictdp[i])
        print "}"
'''

#print dictdp
print processJson(["a","b",34])
print processJson(1)
print processJson("1")
#print type(dictdp)
#print json.dump(dictdp,indent=123)
#processJson(dictdp)
#for i in xrange(1,len(dictdp.keys())+1 ):
#    print i
    #processJson(dict[0])