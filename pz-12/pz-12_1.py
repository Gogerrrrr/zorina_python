#Даны две последовательности. Найти элементы, общие для двух последовательностей и их количество.

from functools import reduce
spis1 = [1, 2, 3, 4, 5, 6]
spis2 = [4, 5, 6, 7, 8, 9]

obsh_elements = list(filter(lambda x: x in spis1, spis2))
kolvo_obsh_elements = len(obsh_elements)

print("Общие элементы:", obsh_elements)
print("Количество общих элементов:", kolvo_obsh_elements)