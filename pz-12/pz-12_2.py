#Из заданной строки отобразить только символы нижнего регистра. ИСпользовать библиотеку
#string. Строка 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
import string
from string import ascii_lowercase as lowers

text = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
lowercase_letters = [x for x in text if x in lowers]
print("Символы нижнего регистра:", lowercase_letters)