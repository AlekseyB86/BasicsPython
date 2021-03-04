"""lesson_8 task_4_5_6"""


# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.
from abc import ABC, abstractmethod


class Storage:
    _count_office_equipment = 0

    def __init__(self):
        _count_office_equipment += 1


class OfficeEquipment:
    bottom_on = False

    def __init__(self, producer, name):
        self._producer = producer
        self._name = name
    
    def __str__(self):
        if isinstance(self._specification(), str):
            return self._specification()
        # raise Exception('')
        
    @abstractmethod
    def _specification(self):
        pass


class Printer(OfficeEquipment):

    def __init__(self, producer, name, color_print, print_type):
        super().__init__(self, producer, name)
        self._color_print = color_print
        self._print_type = print_type

    def _specification(self):
        print(f'Принтер {self._producer} модель {self._name}')


class Scanner(OfficeEquipment):

    def __init__(self, producer, name, color_scanner):
        super().__init__(self, producer, name)
        self._color_scanner = color_scanner

    def _specification(self):
        pass


class Xerox(OfficeEquipment):

    def __init__(self, producer, name, color_copy, ):
        super().__init__(self, producer, name)
        self._color_copy = color_copy

    def _specification(self):
        pass


class MultiFunctionDevice(OfficeEquipment, Printer, Scanner, Xerox):
    pass

    def _specification(self):
        pass


