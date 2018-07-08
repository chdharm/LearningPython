class InputOutString(object):
    def __init__(self):
        self.s="Dharmpal"

    def getString(self):
        self.s=raw_input()

    def printString(self):
        print self.s.upper()

strobj=InputOutString()
strobj.getString()
strobj.printString()