"""lesson_3 task_3"""


# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(x, y, z):
    """возвращает сумму наибольших двух аргументов"""
    max_1 = max(x, y, z)
    if x == max_1:
        result = max_1 + max(y, z)
    elif y == max_1:
        result = max_1 + max(x, z)
    else:
        result = max_1 + max(x, y)
    """2й вариант"""
    # min_1 = min(x, y, z)
    # if x == min_1:
    #     result = y + z
    # elif y == min_1:
    #     result = x + z
    # else:
    #     result = x + y
    return result


print(my_func(2, 5, 6))
