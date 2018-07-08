class BS:
    def binaryS(self,arr,be,en,value):
        middle=(be+en)/2+be
        obj=BS()
        if(be>en):
            return False
        if(arr[middle]==value):
            return True
        elif arr[middle]>value:
            return obj.binaryS(arr,be,middle-1,value)
        else:
            return obj.binaryS(arr, middle +1,en, value)

print BS().binaryS([56,45,334,67,43,2342],0,5,56)