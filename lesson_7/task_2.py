"""lesson 7 task 2"""
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды
# использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу
# этих методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на
# практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def calculate_cloth(self):
        return self._size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    def calculate_cloth(self):
        return 2 * self._height + 0.3


class FabricsCalculate:

    def __init__(self):
        self._fabrics = []

    def add(self, clothes):
        if not isinstance(clothes, Clothes):
            print('Ошибка!')
            return
        self._fabrics.append(clothes)

    def __len__(self):
        return len(self._fabrics)

    def _calculate_fabrics(self):
        return sum(el.calculate_cloth() for el in self._fabrics)

    @property
    def fabrics_total(self):
        return self._calculate_fabrics()


if __name__ == '__main__':
    coat_1 = Coat('Пальто кожаное', 52)
    print(coat_1.calculate_cloth())
    coat_2 = Coat('Пальто шерстяное', 48)
    costume_1 = Costume('Костюм', 186)
    print(costume_1.calculate_cloth())
    costume_2 = Costume('Костюм кашемировый', 190)
    clothes = FabricsCalculate()
    clothes.add(coat_1)
    clothes.add(coat_2)
    clothes.add(costume_1)
    clothes.add(costume_2)
    print(f'Для производства {len(clothes)} типов одежд необходимо {clothes.fabrics_total:.2f} ткани')
