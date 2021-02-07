"""lesson_3 task_3"""


# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.


def my_func_1(x, y, z):
    if x == max(x, y, z):
        result = x + max(y, z)
    elif y == max(x, y, z):
        result = y + max(x, z)
    else:
        result = z + max(x, y)
    return result


def my_func_2(x, y, z):
    if x == min(x, y, z):
        result = y + z
    elif y == min(x, y, z):
        result = x + z
    else:
        result = x + y
    return result


def my_func_3(x, y, z):
    my_list = [x, y, z]
    my_list.remove(min(my_list))
    return sum(my_list)


print(my_func_1(2, 5, 4))
print(my_func_2(4, 5, 2))
print(my_func_3(2, 5, 4))
print((lambda x, y, z: max(x, y) + max(min(x, y), z))(2, 4, 5))

