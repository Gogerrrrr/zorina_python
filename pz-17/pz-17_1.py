#вариант 10
import tkinter as tk
from tkinter import ttk, messagebox

def send_message():
    if not name_entry.get() or not email_entry.get() or not message_text.get("1.0", tk.END).strip():
        messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля!")
    else:
        messagebox.showinfo("Успех", "Ваше сообщение отправлено!")
        # Очистка полей после отправки
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        message_text.delete("1.0", tk.END)
        subject_combobox.set("Product Inquiry")

root = tk.Tk()
root.title("Contact Form")
root.geometry("400x400")

title_label = tk.Label(root, text="Contact Form", font=("Arial", 14, "bold"))
title_label.pack(pady=10)
subtitle_label = tk.Label(root, text="Please fill all entries.", font=("Arial", 10))
subtitle_label.pack()

name_label = tk.Label(root, text="Name:", anchor="w", font=("Arial", 10))
name_label.pack(fill="x", padx=20, pady=(15, 0))
name_entry = tk.Entry(root, font=("Arial", 10))
name_entry.pack(fill="x", padx=20, ipady=3)

email_label = tk.Label(root, text="Email:", anchor="w", font=("Arial", 10))
email_label.pack(fill="x", padx=20, pady=(10, 0))
email_entry = tk.Entry(root, font=("Arial", 10))
email_entry.pack(fill="x", padx=20, ipady=3)

message_label = tk.Label(root, text="Message:", anchor="w", font=("Arial", 10))
message_label.pack(fill="x", padx=20, pady=(10, 0))
message_text = tk.Text(root, height=5, font=("Arial", 10))
message_text.pack(fill="x", padx=20)

subject_label = tk.Label(root, text="Subject:", anchor="w", font=("Arial", 10))
subject_label.pack(fill="x", padx=20, pady=(10, 0))
subject_combobox = ttk.Combobox(root, values=[
    "Product Inquiry",
    "Support",
    "Feedback",
    "Other"
], font=("Arial", 10), state="readonly")
subject_combobox.set("Product Inquiry")
subject_combobox.pack(fill="x", padx=20, ipady=3)

send_button = tk.Button(root, text="Send", command=send_message,
                      bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                      padx=20, pady=5)
send_button.pack(pady=20)

# Запуск главного цикла
root.mainloop()