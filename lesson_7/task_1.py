"""lesson 7 task 1"""
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для
# формирования матрицы. Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, matrix):
        self._main_matrix = matrix

    def __str__(self):
        print()
        new_list = []
        for stroke in self._main_matrix:
            for el in stroke:
                new_list.append(f'{el:^4}')
            new_list.append('\n')
        return ''.join(new_list)

    def __add__(self, other):
        if self._check_matrix(other):
            new_matrix = []
            for idx in range(len(self._main_matrix)):
                small_list = []
                for el in range(len(self._main_matrix[idx])):
                    small_list.append(self._main_matrix[idx][el] + other._main_matrix[idx][el])
                new_matrix.append(small_list)
            return Matrix(new_matrix)
        raise ValueError("Размер матриц не совпадают!")

    def _check_matrix(self, other):
        if len(self._main_matrix) == len(other._main_matrix):
            if len(self._main_matrix[0]) == len(other._main_matrix[0]):
                return True
        else:
            return False


if __name__ == '__main__':
    matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('matrix_1:', matrix_1)

    matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('matrix_2:', matrix_2)

    result_add_2 = matrix_1 + matrix_2
    print('result_add_2:', result_add_2)

    matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('matrix_3:', matrix_3)

    result_add_3 = matrix_1 + matrix_2 + matrix_3
    print('result_add_3:', result_add_3)
