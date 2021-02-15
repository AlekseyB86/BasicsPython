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
with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    f_obj.seek(0)
    content = [stroke.strip() for stroke in f_obj]
rus_number = ['один', 'два', 'три', 'четыре']
new_content = []
i = 0
for el in content:
    new_content.append(rus_number[i] + el[el.index("-") - 1:])
    i += 1
print(new_content)
with open("text_4_1.txt", "w", encoding="utf-8") as f_obj2:
    for el in new_content:
        f_obj2.writelines(f'{el}\n')
