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
from abc import abstractmethod


class OfficeEquipment:
    count = 'шт'

    def __init__(self, name):
        self._name = name

    def __str__(self):
        if isinstance(self._specification(), str):
            return self._specification()
        # raise Exception('')
        
    @abstractmethod
    def _specification(self):
        pass

    @abstractmethod
    def _key(self):
        pass

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._key() == other._key()

    def __hash__(self):
        return hash(self._key())


class Printer(OfficeEquipment):

    def __init__(self, name, print_type):
        super().__init__(name)
        self._print_type = print_type

    def _specification(self):
        return f'Принтер {self._name}, тип печати: {self._print_type}'

    def _key(self):
        return ''.join([self._name, self._print_type])


class Scanner(OfficeEquipment):

    def __init__(self, name, resolution):
        super().__init__(name)
        self._resolution = resolution

    def _specification(self):
        return f'Сканер{self._name}, разрешение: {self._resolution} dpi'

    def _key(self):
        return ''.join([self._name, str(self._resolution)])


class Storage:

    def __init__(self, name):
        self._name = name
        self._stock = {}

    def __str__(self):
        return f'{self._name}'

    def _change_dty(self, products, qty):
        try:
            self._validate_input(products, qty)
        except Exception as err:
            print(err)
        else:
            self._stock[products] = self._stock.setdefault(products, 0) + qty

    def _validate_input(self, products, qty):
        if not isinstance(products, OfficeEquipment):
            raise TypeError(f'Неверный тип товара {type(products)}')
        if not isinstance(qty, int):
            raise TypeError(f'Неверный тип количества {type(qty)}')
        stock = self._current_stock(products)
        if stock + qty > 0:
            f'Товара <{products}> недостаточно на складе. Требуется {abs(qty)}, есть {stock}.'

    def _current_stock(self, products):
        return self._stock.get(products, 0)

    def purchase(self, products, qty):
        self._change_dty(products, qty)

    def requirement(self, products, qty):
        self._change_dty(products, -qty)

    def print_stock(self):
        print(f'Остаток на складе: {self._name}')
        print('\n'.join([f'\t{k}: {str(v)} {k.count}' for k, v in self._stock.items()]))


def main():
    
    storage = Storage('Склад GB')
    storage.purchase(Scanner('Samsung', 600), 5)
    storage.purchase(Printer('Brother', 'laser'), 5)
    storage.purchase(Scanner('Samsung', 600), 4)

    storage.requirement(Scanner('Samsung', 600), 6)
    storage.requirement(Scanner('Samsung', 600), 30)

    print()
    storage.print_stock()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
