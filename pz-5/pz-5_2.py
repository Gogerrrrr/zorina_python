def swap(x, y): #функция по перемешке чисел
    try: #обработка исключений
        x, y = y, x
        return x, y
    except ValueError:
        print("Ошибка, переменые должны быть одинакового типа")
        return x, y

try: #обработка исключений
    a = int(input("Введите число"))
    b = int(input("Введите число"))
    c = int(input("Введите число"))
    d = int(input("Введите число"))
    a, b = swap(a,b)
    c, d = swap (c, d)
    b, c = swap (b, c)
    print("A =", a)
    print("B =", b)
    print("C =", c)
    print("D =", d)
except ValueError:
    print("Ошибка")
