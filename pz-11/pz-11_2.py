#2. Из предложенного текстового файла (text18-13.txt) вывести на экран его содержимое,
#количество букв в нижнем регистре. Сформировать новый файл, в который поместить
#текст в стихотворной форме предварительно поставив последнюю строку фразой введённой
#пользователем.
with open('text18-9.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    lines = content.split('\n')
print("Содержимое файла:")
print(content)

lowercase_letters = sum(1 for char in content if char.islower())
print(f"Количество букв в нижнем регистре: {lowercase_letters}")

new_stroka = input("Введите новую последнюю строку: ")
new_poem = content.strip('\n') + '\n' + new_stroka

with open('new_poem.txt', 'w', encoding='utf-8') as file:
    file.write(new_poem)
print("Новый файл 'new_poem.txt' создан")
