"""lesson_2 task_6*"""
# Реализовать структуру данных «Товары». Она должна представлять собой
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором
# каждый ключ — характеристика товара, например название, а значение —
# список значений-характеристик, например список названий товаров.
i = 1
goods = []
while True:
    product = input('Введите через пробел "название", "цена", "кол-во" '
                    'и "ед" товара (на последнем товаре " .": ').split(" ")
    if product[0] == ".":
        break
    product_Dict = {
        "название": product[0],
        "цена": int(product[1]),
        "кол-во": int(product[2]),
        "ед": product[3]
    }
    product_Tuple = (i, product_Dict)
    goods.append(product_Tuple)
    if product[-1] == ".":
        break
    i += 1
print(*goods, sep='\n')
goods_dict = {}
for m in goods:
    goods_tuple = list(m[1].items())
    for j in goods_tuple:
        if goods_dict.get(j[0]) is None:
            goods_dict[j[0]] = [j[1]]
        else:
            if goods_dict.get(j[0])[0] != j[1]:
                goods_dict.get(j[0]).append(j[1])
for key, value in goods_dict.items():
    print(f"{key}: {value}")
