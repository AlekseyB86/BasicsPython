"""lesson5 task4"""
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.
from translate import Translator

tr = Translator(to_lang='ru')
with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    content = [stroke.strip().split() for stroke in f_obj]
for el in content:
    el.insert(0, tr.translate(el.pop(0)))
content = [' '.join(el) for el in content]
with open("text_4_1.txt", "w", encoding="utf-8") as f_obj2:
    for el in content:
        f_obj2.writelines(f'{el}\n')
