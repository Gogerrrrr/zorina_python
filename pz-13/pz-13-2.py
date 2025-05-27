#в двумерном списке найти среднее арифметическое положительных элементов, кратных 3

def kratnie_3(matrix):
    all_elements = [elem for krat in matrix for elem in krat]
    filtered = list(filter(lambda x: x > 0 and x % 3 == 0, all_elements))
    return sum(filtered) / len(filtered)

matrix = [
    [33, 2, 3],
    [4, 6, -9],
    [7, 9, 12]
]

result = kratnie_3(matrix)
print("Среднее арифметическое положительных элементов, кратных 3:", result)
