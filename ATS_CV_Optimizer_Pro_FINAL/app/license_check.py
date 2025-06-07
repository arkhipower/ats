
import os
from tkinter import messagebox

def check_license():
    license_file = "license.txt"
    if not os.path.exists(license_file):
        messagebox.showerror("Ошибка лицензии", "Файл license.txt не найден.")
        return False
    key = open(license_file, "r", encoding="utf-8").read().strip()
    if key != "PRO-2025-ARKHIPOV":
        messagebox.showerror("Ошибка лицензии", "Неверный лицензионный ключ.")
        return False
    return True
