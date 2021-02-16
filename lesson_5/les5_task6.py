"""lesson5_task6"""
# Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и
# лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
from pprint import pprint
import re


with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    content = [stroke.strip().split() for stroke in f_obj]
    content = {el[0]: sum([int(i) for i in re.findall(r'\d+', el[1])]) for el in content}
pprint(content, sort_dicts=False)
