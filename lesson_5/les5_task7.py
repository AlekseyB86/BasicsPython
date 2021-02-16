"""lesson5_task7"""
# Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать. Далее реализовать список. Он должен содержать
# словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
import json


with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    content = [line.strip().split() for line in f_obj]

content = [[el[0], int(el[2]) - int(el[3])] for el in content]
profit_firms = {el[0]: el[1] for el in content}

salary_profit = sum([el[1] for el in content if el[1] > 0])
count_profit = len([el[1] for el in content if el[1] > 0])
result = round(salary_profit / count_profit, 2)
average_profit = {'average_profit': result}

data = [profit_firms, average_profit]
print(data)

with open("text_77_1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
