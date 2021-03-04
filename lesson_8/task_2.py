"""lesson_8 task_2"""


# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDivisionError(Exception):
    pass


def my_div():
    while True:
        num_1, num_2 = [int(el) for el in input("Введите делимое и делитель через пробел : ").split(' ')]
        try:
            if num_2 == 0:
                raise MyZeroDivisionError("Делить на нуль нельзя!")
            print(f"Результат деления {num_1 / num_2:.2f}")
            break
        except MyZeroDivisionError as err:
            print(f"error: {err}")


if __name__ == '__main__':
    my_div()
