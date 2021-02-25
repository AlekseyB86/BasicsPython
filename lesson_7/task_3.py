"""lesson 7 task 3"""


# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между
# \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в
# последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, count):
        if count > 0:
            self._count = count
        else:
            raise ValueError('Количество ячеек клетки должно быть положительное.')

    def __add__(self, other):
        if self._check_class(other):
            return Cell(self._count + other._count)

    def __sub__(self, other):
        if self._check_class(other):
            result_sub_cell = self._count - other._count
            if result_sub_cell > 0:
                return Cell(result_sub_cell)
            raise ValueError('Результат вычитания клеток должен быть больше нуля.')

    def __mul__(self, other):
        if self._check_class(other):
            return Cell(self._count * other._count)

    def __truediv__(self, other):
        if self._check_class(other):
            return Cell(self._count // other._count)

    def _check_class(self, other_cl):
        if isinstance(other_cl, Cell):
            return True
        raise TypeError(f'{type(other_cl)} не является классом клетки.')

    def __str__(self):
        float_columns = self._count ** 0.5
        columns = int(float_columns) + 1 if float_columns % 1 else int(float_columns)
        return self._make_order(columns)

    def _make_order(self, columns):
        return_list = []
        for numb in range(self._count):
            return_list.append('*')
            if not (numb + 1) % columns:
                return_list.append('\n')
        return ''.join(return_list)

    @property
    def cell_count(self):
        return self._count


if __name__ == '__main__':
    cell_1 = Cell(24)
    cell_2 = Cell(10)
    cell_3 = Cell(8)
    print(f'Клетки К1={cell_1.cell_count}; К2={cell_2.cell_count} и К3={cell_3.cell_count}:\n')
    print(cell_1, '\n')
    print(cell_2, '\n')
    print(cell_3, '\n')

    cell_4 = cell_1 + cell_2
    cell_5 = cell_1 + cell_3 + cell_4
    print(f'Клетки К4=К1+К2={cell_4.cell_count}; К5=К1+К3+K4={cell_5.cell_count}')
    print(cell_4, '\n')
    print(cell_5, '\n')

    cell_6 = cell_5 - cell_4
    cell_7 = cell_1 - cell_2 - cell_3
    print(f'Клетки К6=К5-К4={cell_6.cell_count}; К7=К1-К2-K3={cell_7.cell_count}')
    print(cell_6, '\n')
    print(cell_7, '\n')

    cell_8 = cell_1 * cell_2
    cell_9 = cell_7 * cell_3 * cell_2
    print(f'Клетки К8=К1*К2={cell_8.cell_count}; К9=К7*К3*K2={cell_9.cell_count}')
    print(cell_8, '\n')
    print(cell_9, '\n')

    cell_10 = cell_1 / cell_2
    cell_11 = cell_9 / cell_2 / cell_7
    print(f'Клетки К10=К1/К2={cell_10.cell_count}; К11=К9/К2/K7={cell_11.cell_count}')
    print(cell_10, '\n')
    print(cell_11, '\n')
