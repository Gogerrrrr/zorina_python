#Арифметические действия над числами пронумерованы следующим образом: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление.
#Дан номер действия N и вещественные числа А и В(В не равно нулю)
#Выполнить над числами указанное действия и вывести результат

try:#обработка исключений
    N = int(input("Выберите действие: 1 - сложение, 2 - вычитание, 3 - умножение, 4 - деление:"))
    a = int(input("Введите число а:"))
    b = int(input("Введите число b:"))
    if N == 1:#проверки условия
        result = a + b
        print("Результат сложения:", result)
    elif N == 2:
        result = a - b
        print("Результат вычитания:", result)
    elif N == 3:
        result = a * b
        print("Результат умножения:", result)
    elif N == 4:
        result = a / b
        print("Результат деления:", result)
except ValueError: #возвращение на try
    print("Введите корректные числа!")
