def fact(num):
    if(num<2):
        return num
    return num*fact(num-1)
num=input('Enter number for factorial calculation')
print type(num)
print fact(num)