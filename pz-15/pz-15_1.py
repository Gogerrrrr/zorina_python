#Приложение учебный план для автоматизированного контроля учебной нагрузки по кафедре.
#Таблица Дисциплины должна иметь следующую структуру записи:
#Код дисциплины, Наименование дисциплины, Специальность, Лекции(кол-во часов), Практические(кол-во часов), Лабораторные(кол-во часов), Форма отчетности
try:
    import sqlite3

    # Создание и подключение к базе данных
    conn = sqlite3.connect('ychebniplan.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS disciplines (
        id_disciplini INT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        specialnost VARCHAR(50) NOT NULL,
        lectures INT NOT NULL,
        practical INT NOT NULL,
        laboratory INT NOT NULL,
        froma_otchet VARCHAR(10) NOT NULL
    )
    ''')
    conn.commit()


    def add_disciplines():
        print("\nДобавление новой дисциплины:")
        id_disciplini = input("Код специальности: ")
        name = input("Наименование: ")
        specialnost = input("Специальность: ")
        lectures = int(input("Часы лекций: "))
        practical = int(input("Часы практических: "))
        laboratory = int(input("Часы лабораторных: "))
        froma_otchet = input("Форма отчётности: ")

        cursor.execute('''
        INSERT INTO disciplines 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (id_disciplini, name, specialnost, lectures, practical, laboratory, froma_otchet))
        conn.commit()
        print("Дисциплина успешно добавлена!")


    def view_disciplines():
        print("\nСписок дисциплин:")
        cursor.execute("SELECT * FROM disciplines")
        disciplinii = cursor.fetchall()

        if not disciplinii:
            print("Нет данных о дисциплине.")
        else:
            for disciplina in disciplinii:
                print(f"""
                Код дисциплины: {disciplina[0]}
                Наименование: {disciplina[1]}
                Специальность: {disciplina[2]}
                Часы лекций: {disciplina[3]}
                Часы практических: {disciplina[4]}
                Часы лабораторных: {disciplina[5]}
                Форма отчётности: {disciplina[6]}
                """)


    def update_disciplina():
        id_disciplini = input("Введите код дисциплины для изменения: ")
        cursor.execute("SELECT * FROM disciplines WHERE id_disciplini=?", (id_disciplini,))
        disciplina = cursor.fetchone()

        if not disciplina:
            print("Дисциплина не найдена!")
            return

        print(f"Код дисциплины: {disciplina[1]}:")
        print(f"1. Наименование: {disciplina[1]}")
        print(f"2. Специальность: {disciplina[2]}")
        print(f"3. Часы лекций: {disciplina[3]}")
        print(f"4. Часы практических: {disciplina[4]}")
        print(f"5. Часы лабораторных: {disciplina[5]}")
        print(f"6. Форма отчётности: {disciplina[6]}")

        field = input("Выберите номер поля для изменения (1-6): ")
        new_value = input("Введите новое значение: ")

        fields = {
            '1': 'name',
            '2': 'specialnost',
            '3': 'lectures',
            '4': 'practical',
            '5': 'laboratory',
            '6': 'forma_otchet'
        }

        cursor.execute(f'''
        UPDATE disciplines 
        SET {fields[field]} = ? 
        WHERE id_disciplini = ?
        ''', (new_value, id_disciplini))
        conn.commit()
        print("Данные успешно обновлены!")


    def delete_disciplini():
        id_disciplini = input("Введите код дисциплины для удаления: ")
        cursor.execute("DELETE FROM disciplines WHERE id_disciplini=?", (id_disciplini,))
        conn.commit()
        print("Дисциплина удалена!" if cursor.rowcount else "Дисциплина не найдена!")


    def main_menu():
        while True:
            print("\n=== Дисциплина ===")
            print("1. Добавить дисциплину")
            print("2. Просмотреть все дисциплины")
            print("3. Изменить данные дисциплин")
            print("4. Удалить дисциплину")
            print("5. Выход")

            choice = input("Выберите действие (1-5): ")
            if choice == '1':
                add_disciplines()
            elif choice == '2':
                view_disciplines()
            elif choice == '3':
                update_disciplina()
            elif choice == '4':
                delete_disciplini()
            elif choice == '5':
                print("Работа завершена.")
                break
            else:
                print("Некорректный ввод!")


    if __name__ == "__main__":
        main_menu()
        conn.close()

except ValueError:
    print("Ошибка")
