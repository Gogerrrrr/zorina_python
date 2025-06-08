#Создание базового класса "РАботник" и его наследование для создания классов
#"Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как "работать" и
#"получать зарплату", а классы наследники будут иметь свои уникальные методы, такие как
#"управлять командой" и "проектировать системы"

class rabotnik:
    def __init__(self, name, zp):
        self.name = name
        self.zp = zp

    def work(self):
        print(f"{self.name} работает отлично, выполняет все свои обязанности")

    def zpshka(self):
        print(f"{self.name} получает зарплату {self.zp} рубликов")


class Meneger(rabotnik):
    def ypravlenie_komandoi(self):
        print(f"\n{self.name} управляет командой сотрудников")


class Engineer(rabotnik):
    def proektirovanie_sistem(self):
        print(f"\n{self.name} проектирует системы")

Meneger = Meneger("Алексей", 130000)
Engineer = Engineer("Олегш", 85000)
rabotnik = rabotnik("Ольга", 67000)

rabotnik.work()
rabotnik.zpshka()

Meneger.work()
Meneger.zpshka()

Engineer.work()
Engineer.zpshka()

Meneger.ypravlenie_komandoi()
Engineer.proektirovanie_sistem()