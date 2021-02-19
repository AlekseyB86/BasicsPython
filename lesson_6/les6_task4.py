"""lesson6 task4"""


# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    is_police = False
    speed_limit = 60

    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.direction = None

    def go(self, go_speed=None):
        self.speed = go_speed or self.speed
        if self.speed:
            print(f'Машина {self.name} едет.', end=' ')
            self.show_speed()
        else:
            print('Машина стоит на месте, т.к. скорость не указана.')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Превышена максимальная допустимая скорость на {self.speed - self.speed_limit} км/ч')


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Превышена максимальная допустимая скорость на {self.speed - self.speed_limit} км/ч')


class PoliceCar(Car):
    speed_limit = None

    def __init__(self, color, name):
        super().__init__(color, name)
        self.is_police = True

    def show_speed(self):
        super().show_speed()


town_car = TownCar('чёрный', 'Honda')
print(f'Имя: {town_car.name} | Цвет: {town_car.color} | Текущая скорость: {town_car.speed} |'
      f' Полицейская: {town_car.is_police} | Огроничение по скорости: {town_car.speed_limit} км/ч')
town_car.go()
town_car.go(70)
town_car.go(50)
town_car.turn('на право')
town_car.stop()
print()

work_car = WorkCar('синий', 'УАЗ-3909')
print(f'Имя: {work_car.name} | Цвет: {work_car.color} | Текущая скорость: {work_car.speed} |'
      f' Полицейская: {work_car.is_police} | Огроничение по скорости: {work_car.speed_limit} км/ч')
work_car.go()
work_car.go(100)
work_car.go(20)
work_car.turn('назад')
work_car.stop()
print()

police_car = PoliceCar('сине-белый', 'Жигуль')
print(f'Имя: {police_car.name} | Цвет: {police_car.color} | Текущая скорость: {police_car.speed} |'
      f' Полицейская: {police_car.is_police} | Огроничение по скорости: {police_car.speed_limit} км/ч')
police_car.go()
police_car.go(170)
police_car.go(80)
police_car.turn('на право')
police_car.stop()
print()
