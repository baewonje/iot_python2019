class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
        
    def setdata(self,first, second):
        self.first = first # 멤버 변수가 없음에도 객체생성이후에
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first - self.second
        return result

    def sub(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def print_number(self):
        print("first: %d, second: %d"%(self.first,self.second))

class MoreFourCal(FourCal):
    pass

a= FourCal(4,2)

child = MoreFourCal(1,2)
# child.print_number()
print(child.add())