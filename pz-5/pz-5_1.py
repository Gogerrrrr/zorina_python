
import random

def generate_number(): #вызов функции, генерация чисел
    try: #обработка исключений
        number = random.randint(1000, 9999)
        if chk_dubls(number):
            print(f"Число {number} содержит одинаковые числа")
        else:
            print('Число', number, 'не содержит одинаковых чисел')
    except ValueError:
        print("Произошла ошибка")

def chk_dubls(number): #вызов функции проверка на дубликаты чисел
    return len(set(str(number))) != 4
print(generate_number())
