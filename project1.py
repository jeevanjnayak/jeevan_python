class Calculator():
    def sum(self):
        result = self.num1 + self.num2
        print(result)


    def multiply(self):
        result = self.num1 * self.num2
        print(result)


num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
obj =  Calculator()
obj.num1 = num1
obj.num2 = num2
obj.sum()
obj.multiply()