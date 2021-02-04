"""lesson_2 task_2"""
# Для списка реализовать обмен значений соседних элементов,
# (Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.)
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов использовать функцию input().
my_list = []
user_Element = input("Введиет эелемент списка: ")
while user_Element not in ['off', 'нет']:
    my_list.append(user_Element)
    user_Element = input("Добавьте элемент в список (выход-'no'): ")
print(my_list)
for i in range(0, len(my_list)-1, 2):
    my_list.insert(i + 1, my_list.pop(i))
print(my_list)
