
#3

class Calc:
    def __init__(self, value =0):
        self.value = value
        
    def setvalue(self, value):
        self.value = value
        return self.value

    def add(self, num):
        self.value += num

    def minus(self, num):
        self.value -= num

    def print(self):
        print(self.value)

    def getvalue(self):
        return self.value

cal1 = Calc()

cal2= Calc(5)

cal1.setvalue(10)

cal1.add(20)
cal1.print()

cal1.minus(5)
cal1.print()

cal2.add(cal1.getvalue())

cal2.print()
        
