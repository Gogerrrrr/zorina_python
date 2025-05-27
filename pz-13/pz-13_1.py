#В двумерном списке элементы второго стобца заменить элементами из
#одномерного динамического массива соответствующей размерности
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_column = [1, 114, 534]
def replace_second_column(matrix, new_column):
    return list(map(lambda x, zamena: x[:1] + [zamena] + x[2:], matrix, new_column))

result = replace_second_column(matrix, new_column)
print("Результат замены второго столбца:")
for x in result:
    print(x)
