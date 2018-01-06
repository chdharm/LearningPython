n=input("Enter the date to check:")
dd,mm,yy=n.split('/')
day=int(dd)
month=int(mm)
year=int(yy)
print "Day:",day,"Month:",month,"Year:",year
if year%4==0 and year%100==0 or year%400==0:
    print "This is leap year."
else:
    print "This is not leap year."