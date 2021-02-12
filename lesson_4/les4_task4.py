"""lesson_4 task_4"""
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

# numbers = [2, 2, 'a', 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# Усложним задачу
from random import randint

count_chars = 20
numbers = [randint(0, 30) for el in range(count_chars)]
not_numbers = [chr(randint(65, 100)) for ch in range(count_chars // 2)]
numbers.extend(not_numbers)
print(numbers)

numbers_unique = [el for el in numbers if numbers.count(el) == 1 and type(el) != str]
print('Уникальные числа: ', numbers_unique)
numbers_repeating = {el: numbers.count(el) for el in numbers if numbers.count(el) > 1 and type(el) != str}
print('Повторяющиеся числа: ', numbers_repeating)
other_symbol = {el: numbers.count(el) for el in numbers if type(el) == str}
print('Не числа: ', other_symbol)
