range1 = int(input("enter the range you want to go: "))
a = 0
b = 1
c = 0
print(a)
# while c <= range1:
#     c = a + b
#     print(b)
#     a = b
#     b = c
for c in range(range1):
    c = a + b
    print(b)
    a = b
    b = c