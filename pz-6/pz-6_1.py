#Дан целочисленный список размера 10. Вывести вначале
#Содержащиеся в данном списке четные числа в порядке возрастания,
#а затем - все нечетные числа в порядке убывания

def sort_chet_nechet_numbers(numbers): #сортируем четные и нечетные числа
    chet_numbers = []
    nechet_numbers = []

    for number in numbers:
        if number % 2 == 0:
            chet_numbers.append(number)
        else:
            nechet_numbers.append(number)
    return chet_numbers, nechet_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

chet_numbers, nechet_numbers = sort_chet_nechet_numbers(numbers)

print("Четные числа в порядке возрастания: ")
for number in chet_numbers:
    print(number)
print("нечетные числа в порядке убывания: ")
for number in reversed(nechet_numbers):
    print(number)
