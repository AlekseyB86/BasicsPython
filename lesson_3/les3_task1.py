"""lesson_3 task_1"""
# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def my_func(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        print(int(result) if result.is_integer() else round(result, 3))
    except ValueError:
        print('Введено не число!')
    except ZeroDivisionError:
        print('Нельзя делить на 0!')


x = input('Введите первое число: ')
y = input('Введите второе число: ')
my_func(x, y)
