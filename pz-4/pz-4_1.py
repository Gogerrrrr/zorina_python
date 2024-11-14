#дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3...+ 1/N
while True:
    try:#обработка исключений
        n = int(input("Введите число N:"))
        sum = 0
        for i in range(1, n + 1):
            sum += 1 / i
            print("Сумма равна:", sum)
        break
    except ValueError:#возвращение на try
        print("Введите корректное число!")
