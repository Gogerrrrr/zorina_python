matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = int(input("Введите номер столбца (от 0): "))

new_matrix = list(map(
    lambda row: [val * 2 if i == n else val for i, val in enumerate(row)],
    matrix
))

print("Результат:")
for row in new_matrix:
    print(row)