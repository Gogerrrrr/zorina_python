#Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение"
#и "деление". Каждый метод должен принимать два аргумента и возвращать результат операции

class Calculator:
    def __init__(self):
        self.result = None

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b == 0 or a == 0:
            raise ValueError("Деление на ноль невозможно")
        self.result = a / b
        return self.result

    def get_last_result(self):
        return self.result

calc = Calculator()

a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
print("Калькулятор с методами сложения, вычитания, умножения и деления:")
print("Сложение:", calc.add(a, b))
print("Вычитание:", calc.subtract(a, b))
print("Умножение:", calc.multiply(a, b))
try:
    print("Деление:", calc.divide(a, b))
except ValueError:
    print("Делить на ноль НЕЛЬЗЯЯЯЯ!!!!!!!!!!!!!!!!!")