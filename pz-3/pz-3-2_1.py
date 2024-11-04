a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
c = a * b
print(c)
if c < 0:
    result = c * 8
    print(result)
else:
    result = c * 1.5
    print(result)