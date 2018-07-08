class ParameterPass:
    def __init__(self):
        A=[1,2,3,4,5]
        self.Change(A)
        print A
    def Change(self,li):
        li.append(6)
print ParameterPass()
#print ParameterPass.