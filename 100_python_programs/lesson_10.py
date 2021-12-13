class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
        t = self.s
    def printString(self):
        l = t.upper()
        print(l)

strObj = InputOutString()
strObj.getString()
strObj.printString()