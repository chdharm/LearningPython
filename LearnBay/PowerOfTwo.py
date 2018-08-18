#we can check set bits if it's one then it's power of two

def isPowerOfTwo(x):
    if x==0:
		print ('true')
        return
    if (x&(x-1))==0:
		print ('true')
    else:
		print('false')

if __name__=='__main__':
    isPowerOfTwo(0)