# #First Method Iterative#
# def rev1(num):
#     res=0
#     while(num>0):
#         res=res*10+(num%10)
#         num=num/10
#     return res
#
# if __name__=='__main__':
#     print rev1(67527565)
#Second Method Recursive#
def rev2(num):
    if num == 0:
        return ''
    return str(num % 10) + rev2(num / 10)
#Enter the number
num=input()
#print rev1(num)
print int(rev2(num))