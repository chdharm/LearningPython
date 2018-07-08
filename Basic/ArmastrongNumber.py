def isArmastrong(num):
  temp=num
  r=0
  sum=0
  while(num>0):
      r=num%10
      num=num/10
      sum=sum+(r*r*r)
  if temp==sum:
      return True
  else:
      return False
if __name__=='__main__':
    result=isArmastrong(153)
    if result==True:
        print "The number is armastrong"
    else:
        print "The number is not armastrong"