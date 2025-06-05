#в двумерном списке найти среднее арифметическое положительных элементов, кратных 3
import random
rows = 3
columns = 3
matrix = []
for i in range(rows):
    row = [random.randint(1, 100) for i in range(columns)]
    matrix.append(row)
print("Исходная матрица:")
for row in matrix:
    print(row)

def kratnie_3(matrix):
    all_elements = [elem for krat in matrix for elem in krat]
    filtered = list(filter(lambda x: x > 0 and x % 3 == 0, all_elements))
    return sum(filtered) / len(filtered)

result = kratnie_3(matrix)
print("Среднее арифметическое положительных элементов, кратных 3:", result)
