"""lesson 6 task 5"""


# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        if self.title:
            print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'Ручка: {self.title or ""}.')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'Карандаш: {self.title or ""}.')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'Маркер: {self.title or ""}.')


pen_1 = Pen("Parker")
pen_1.draw()

pen_2 = Pencil('Карандаш')
pen_2.draw()

pen_3 = Handle("Marker")
pen_3.draw()
