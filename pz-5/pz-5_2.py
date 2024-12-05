def swap(x, y):
    try:
        x, y = y, x
        return x, y
    except ValueError:
        print("Ошибка, переменые должны быть одинакового типа")
        return x, y
a = int(input("Введите число"))
b = int(input("Введите число"))
c = int(input("Введите число"))
d = int(input("Введите число"))

try:
    a, b = swap(a,b)
    c, d = swap (c, d)
    b, c = swap (b, c)
    print("A =", a)
    print("B =", b)
    print("C =", c)
    print("D =", d)
except ValueError:
    print("Ошибка")