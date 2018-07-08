def power(num,pow):
    if(pow==0):
        return 1
    if pow==1:
        return num
    return num*power(num,pow-1)

print power(2,5)