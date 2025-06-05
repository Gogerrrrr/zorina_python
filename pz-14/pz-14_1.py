# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии Достоевского
# (т.е. с различными окончаниями, например, Достоевский, Достоевского) в единственном экземляре
import re
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

familii = re.findall(r"\bДостоевск\w+\b", text)
unique = set(familii)

print("варианты написания фамилии <<Достоевский>>:")
for word in unique:
    print(word)