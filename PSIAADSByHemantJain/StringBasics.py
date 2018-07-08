# stri="DharmpalChaudhary"
# print 'i' in stri
class StringOp:
    @classmethod
    def printsum(cls,num):
        sum=0
        while num>0:
            sum=sum+num%10
            num=num/10
        return sum

print StringOp.printsum(6565472357243)