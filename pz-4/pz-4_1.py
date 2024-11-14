while True:
    try:
        n = int(input("Введите число N:"))
        summa = 0
        for i in range(1, n + 1):
            summa = 1 / i
            print("Сумма равна:", summa)
        break
    except ValueError:
        print("Введите корректное число!")