#Приложение учебный план для автоматизированного контроля учебной нагрузки по кафедре.
#Таблица Дисциплины должна иметь следующую структуру записи:
#Код дисциплины, Наименование дисциплины, Специальность, Лекции(кол-во часов), Практические(кол-во часов), Лабораторные(кол-во часов), Форма отчетности
import sqlite3
conn = sqlite3.connect('ycebnyplan.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS disciplines (
                          id_disciplini INT PRIMARY KEY,
                          name VARCHAR(50) NOT NULL,
                          specialnost CHAR(50) NOT NULL,
                          lectures INT NOT NULL,
                          practical INT NOT NULL,
                          laboratory INT NOT NULL,
                          forma_otchet CHAR(50) NOT NULL)''')
conn.commit()
def dobavit():
    print("\nДобавить информацию:")
    id_disciplini = int(input("Код дисциплины: "))
    name = input("Наименование дисциплины: ")
    specialnost = input("Специальность: ")
    lectures = int(input("Кол-во часов: "))
    practical = int(input("Кол-во часов: "))
    laboratory = int(input("Кол-во часов: "))
    forma_otchet = input("Форма отчётности: ")
sql = '''INSERT INTO disciplines(id_disciplini, name, specialnost, lectures, practical, laboratory, forma_otchet)",
            VALUES(?,?,?,?,?,?,?)'''
cursor = conn.cursor()
cursor.execute(sql, disciplines)
conn.commit()