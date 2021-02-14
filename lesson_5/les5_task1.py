"""lesson5 task1"""
# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.
with open("text.txt", "w", encoding="utf-8") as f_obj:
    str_line = input("Введите строку и нажмите ENTER: ")
    while len(str_line) > 0:
        f_obj.writelines(f"{str_line}\n")
        str_line = input("Введите ещё строку или для выхода нажмите ENTER: ")

with open("text.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        print(line, end="")
