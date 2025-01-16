#ДАна непустая строка. Вывести коды ее первого и последнего символа
text = input("Введите текст:")


first_symbol = text[0]
last_symbol =  text[-1]

first_symbol_code = ord(first_symbol)
last_symbol_code = ord(last_symbol)

print(f"Код первого символа: {ord(text[0])}")
print(f"Код последнего символа: {ord(text[-1])}")