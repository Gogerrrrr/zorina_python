#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Индекс первого максимального элемента:
#Меняем местами первую и последнюю трети:

import math

with open('input(number).txt', 'w', encoding='utf-8') as file:
    file.write("1 -1 2 -2 3 -3 4 -4 5 -5 6 -6 7 -7 8 -8")
with open('input(number).txt', 'r', encoding='utf-8') as file:
    numbers = list(map(int, file.read().split()))

kolvo = len(numbers) #Количество элементов

max_index = numbers.index(max(numbers)) #Индекс первого максимального элемента

third = len(numbers) // 3
first_part = numbers[:third]
middle_part = numbers[third:-third]
last_part = numbers[-third:]
new_numbers = last_part + middle_part + first_part

with open('output(number).txt', 'w', encoding='utf-8') as file:
    file.write("Исходные данные: " + ' '.join(map(str, numbers)) + "\n")
    file.write("Количество элементов: " + str(kolvo) + "\n")
    file.write("Индекс первого максимального элемента: " + str(max_index) + "\n")
    file.write("Меняем местами первую и последнюю трети: " + str(new_numbers) + "\n")