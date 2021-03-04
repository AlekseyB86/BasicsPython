"""lesson_8 task_7"""


# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.complex = f'{self.num_1} + {self.num_2}j'

    def __add__(self, other):
        num_left = self.num_1 + other.num_1
        num_right = self.num_2 + other.num_2
        return self.__class__(num_left, num_right)

    def __mul__(self, other):
        num_left = (self.num_1 * other.num_1) - (self.num_2 * other.num_2)
        num_right = (self.num_1 * other.num_2) + (self.num_2 * other.num_1)
        return self.__class__(num_left, num_right)

    def __str__(self):
        return self.complex


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
print(f'a + b = ({a}) + ({b}) = {a + b}')
print(f'a * b = ({a}) * ({b}) = {a * b}')
