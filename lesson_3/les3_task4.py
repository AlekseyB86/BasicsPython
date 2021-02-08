"""lesson_3 task_4"""


# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в
# виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
# с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def my_func_1(x, y):
    """Программа принимает действительное положительное число x и целое отрицательное число y и
    выполняет возведение числа x в степень y"""
    try:
        if x < 0 or 0 < y:
            raise Exception
        return x ** int(y)
    except ValueError or ZeroDivisionError:
        print('Функции переданы неверные параметры! x > 0! и y < 0')


def my_func_2(x, y):
    if x > 0 > int(y):
        res = 1
        for i in range(-y):
            res = res / x
        return res
    else:
        print('Функции переданы неверные параметры! x > 0! и y < 0')


def my_func_3(x, y):
    if x <= 0 or 0 < y:
        print('Функции переданы неверные параметры! x > 0! и y < 0')
    elif int(y) == 0:
        return 1
    else:
        return my_func_3(x, y + 1) / x


print(my_func_1(0, -2))
print(my_func_2(0, -2))
print(my_func_3(0, -2))
