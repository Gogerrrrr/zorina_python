# Составить программу, в которой функция генерирует четрыехзначное число и определяет,
# есть ли в числе одинаковые цифры
import tkinter as tk
import random


def generate_and_check():
    # Генерация четырехзначного числа
    number = random.randint(1000, 9999)
    number_str = str(number)

    # Проверка на одинаковые цифры
    has_duplicates = len(set(number_str)) < len(number_str)

    number_label.config(text=f"Сгенерированное число: {number_str}")
    if has_duplicates:
        result_label.config(text="В числе есть одинаковые цифры", fg="red")
    else:
        result_label.config(text="Все цифры в числе уникальны", fg="green")


root = tk.Tk()
root.title("Генератор чисел и проверка цифр")
root.geometry("400x200")

title_label = tk.Label(root, text="Генерация четырехзначного числа и проверка цифр", font=("Arial", 12))
title_label.pack(pady=10)

generate_button = tk.Button(root, text="Сгенерировать и проверить", command=generate_and_check)
generate_button.pack(pady=10)

number_label = tk.Label(root, text="Сгенерированное число: ----", font=("Arial", 10))
number_label.pack(pady=5)

result_label = tk.Label(root, text="Результат проверки: ----", font=("Arial", 10))
result_label.pack(pady=5)

root.mainloop()