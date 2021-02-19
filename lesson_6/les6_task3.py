"""lesson6 task3"""


# Реализовать базовый класс Worker (работник), в котором определить
# атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса
# Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        total_income = sum(self._income.values())
        return f'Доход с учетом премии составляет: {total_income} уе'


user_1 = Position('Иван', 'Иванов', 'босс', 10_000, 300)
print(user_1.name)
print(user_1.surname)
print(user_1.get_full_name())
print(user_1.get_total_income())
