def pypart(n):
    for i in range(0,n):
        for j in range(0,n):
            if j<n-i-1:
                print " ",
            else:
                print "*",
        print

pypart(5)



'''
C:\Python27\python.exe C:/Users/Admin/PycharmProjects/FirstProject/Third.py
        *
      * *
    * * *
  * * * *
* * * * *


'''