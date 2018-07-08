dict={}
n=input("Enter the number of elements")
for i in range(n):
    num=input()
    if dict.has_key(num):
        dict[num]=dict[num]+1
    else:
        dict[num]=1
l=len(dict)
for k in dict.keys():
    if dict[k]>1:
        print k
# for k,v in dict:
#     if v>0:
#         print k