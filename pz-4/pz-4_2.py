def summa_drobey(k):
    sum = 0
    for i in range(1, k + 1):
        sum += 1 / i
    return sum
def find_small_k(a):
    k = 1
    while summa_drobey(k) <= a:
        k += 1
    return k, summa_drobey(k)
while True:
    try:
        a = int(input("Введите число A (>1): "))
        if a > 1:
            break
        else:
            print("Ошибка: A должно быть больше 1.")
    except ValueError:
        print("Ошибка: Введите число.")

k =  find_small_k(a)
sum = find_small_k(a)
print("Наименьшее K:", k)
print("Сумма:", sum)
