# def convertIntoBinary(num,b):
#     res=0
#     i=0
#     while num>0 and i<=b:
#       res=res+(num%10)*(2**i)
#       num=num/10
#       i=i+1
#     return res


# def binaryToDecimal(binary):
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while (binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary // 10
#         i += 1
#     return decimal
def binaryToDecimal(stri):
    return int(stri, 2)
if __name__=='__main__':
    # print convertIntoBinary(1010,4)
    # print convertIntoBinary(0100, 4)
    # print convertIntoBinary(0010, 4)
    # print convertIntoBinary(0011, 4)
    print binaryToDecimal('1010')
    print binaryToDecimal('0100')
    print binaryToDecimal('0010')
    print binaryToDecimal('0011')
    # arr=raw_input().split()
    # a=int(arr[0])
    # b=int(arr[0])
    # print a,'--',b
    # max=0
    # for i in range(a):
    #     num=input()
    #     t=convertIntoBinary(num,b-1)
    #     if t>max:
    #         max=t
    # print max