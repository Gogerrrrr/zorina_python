#В двумерном списке элементы второго столбца заменить элементами из
#одномерного динамического массива соответствующей размерности
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

new_column = [random.randint(1, 100) for i in range(rows)]
for i in range(rows):
    matrix[i][1] = new_column[i]

print("Матрица после замены второго столбца:")
for row in matrix:
    print(row)
