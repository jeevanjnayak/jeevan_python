a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
operator = input("enter the operator (+ or - or * or / ): ")
result = 0
if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    result = a / b
else:
    print("you entered a wrong operator.")
print(f"result = {result}")