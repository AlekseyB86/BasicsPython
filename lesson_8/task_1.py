"""les_8 task_1"""
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import re


class InvalidDateError(Exception):
    pass


class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def get_int_date(cls, date):
        date_list = re.compile(r'\W+')
        date_list = date_list.split(date)
        cls.is_valid(date_list)
        date = list(map(int, date_list))
        return date
        # return cls(date)

    @staticmethod
    def is_valid(date_list):
        if all(el.isdigit() for el in date_list) and len(date_list) == 3:
            if 1 > int(date_list[0]) > 31 or 1 > int(date_list[1]) > 12:
                raise InvalidDateError('input date is nod valid!')
        else:
            raise InvalidDateError('input date is nod valid!')


if __name__ == "__main__":
    try:
        print(Date.get_int_date('12,14-1225'))
    except InvalidDateError as e:
        print(f'error: {e}')
