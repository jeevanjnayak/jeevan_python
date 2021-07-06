a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

result = {}

addition = a + b

subtraction = a - b

multiplication = a * b

result["sum"] = addition
result["difference"] = subtraction
result["product"] = multiplication
print(result)