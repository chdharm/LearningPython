import re,json

#Two simple object comparision
def compareJson(d1,d2):
    uni1=[]
    uni2=[]
    common=[]
    commondiffval=[]
    all_keys1=d1.keys()
    all_keys2=d2.keys()
    for key in all_keys1:
        if key not in all_keys2:
            uni1.append(key)
        elif d1[key]==d2[key]:
            common.append(key)
        elif d1[key]!=d2[key]:
            commondiffval.append(key)
    for key in all_keys2:
        if key not in all_keys1:
            uni2.append(key)
    return {"Matching":common,"MatchingKeyNotValue":commondiffval,"OnlyInOne":uni1,"OnlyInTwo":uni2}


if __name__=='__main__':
    d1={
        "First":"Dharmpal",
        "Second":"Chaudhary",
        "Education":"Btech"
    }
    d2={
        "First": "Sandhya",
        "Second": "Chaudhary",
        "Age": "21"
    }
    result=compareJson(d1,d2)
    print type(result)
    print result


