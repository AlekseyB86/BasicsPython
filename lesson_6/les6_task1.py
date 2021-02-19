"""lesson6 task1"""
# Создать класс TrafficLight (светофор) и определить у него один атрибут
# color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.
import time
from itertools import cycle


class TrafficLight:
    def __init__(self, color='Black'):
        self._color = color
        self.tuple_color = ('RED', 'YELLOW', 'GREEN')

    def running(self, color_time):
        self._check_order(color_time)
        for color, timer in cycle(color_time.items()):
            self._color = color
            print(self._color)
            time.sleep(timer)

    def _check_order(self, color_time):
        if self.tuple_color != tuple(color_time.keys()):
            return print("Нарушен порядок работы светофора!")


traffic_light_1 = TrafficLight()
traffic_light_1.running({'RED': 7, 'YELLOW': 2, 'GREEN': 5})
