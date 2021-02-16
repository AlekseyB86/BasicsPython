"""lesson5 task5"""
# Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.
from random import randint

list_numbers = [str(randint(0, 10)) for el in range(10)]
with open("text5.txt", "w", encoding="utf-8") as f_obj:
    f_obj.write(' '.join(list_numbers))
with open("text5.txt", "r", encoding="utf-8") as f_obj:
    content = f_obj.read().split()
print(content)
print(sum([int(el) for el in content]))
