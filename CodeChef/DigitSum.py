def getSum(num):
	res=0
	while num>0:
		res=res+(num%10)
		num=num/10
	return res
if __name__=='__main__':
	t=input()
	for i in range(t):
		num=input()
		print getSum(num)