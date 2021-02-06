"""lesson_3 task_1"""
# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def my_func(s_1, s_2):
    try:
        result = s_1 / s_2
        return int(result) if result.is_integer() else round(result, 3)
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')


try:
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))
except ValueError:
    print("Необходимо ввести число!")

print(my_func(number_1, number_2))
