"""lesson5 task3"""
# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
from pprint import pprint
with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    f_obj.seek(0)
    content = [stroke.strip().split() for stroke in f_obj]
content = {el[0]: float(el[1]) for el in content}
employees_low_salary = [surname for surname in content if content[surname] < 20000]
# 1й вариант
# print(f'Сотрудники с окладом меньше 20 тыс.: {", ".join(employees_low_salary)}')

# 2й вариант
print('Сотрудники с окладом меньше 20 тыс.:')
pprint({key: value for key, value in content.items() if value < 20000})

print(f'Средняя величина дохода сотрудников: {sum(content.values()) / len(content):.2f}')
