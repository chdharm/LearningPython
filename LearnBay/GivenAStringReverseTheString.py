#Simple iterative approach
def reverse(str):
    res=""
    for i in str:
        res=i+res
    return res
if __name__=='__main__':
    str=input()
    print reverse(str)
