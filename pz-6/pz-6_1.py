#Дан целочисленный список размера 10. Вывести вначале
#Содержащиеся в данном списке четные числа в порядке возрастания,
#а затем - все нечетные числа в порядке убывания
numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sort_chet_nechet_numbers(numbers): #сортируем четные и нечетные числа
    chet_numbers = []
    nechet_numbers = []

    for number in numbers:
        if number % 2 == 0:
            chet_numbers.append(number)
        else:
            nechet_numbers.append(number)
    return chet_numbers, nechet_numbers


chet_numb, nechet_numb = sort_chet_nechet_numbers(numb)

print("Четные числа в порядке возрастания: ")
for number in chet_numb:
    print(number)
print("нечетные числа в порядке убывания: ")
for number in reversed(nechet_numb):
    print(number)
