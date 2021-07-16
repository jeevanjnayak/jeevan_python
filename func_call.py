from function_main import add, subtract, multiplication, division


x = int(input("enter the first number: "))
y = int(input("enter the second number: "))

add(x, y)
subtract(x, y)
multiplication(x, y)

try:
    division(x, y)
except:
    print("can't devide by zero")