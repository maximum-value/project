#  Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
#  инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
#  методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
#  деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
#  умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
#  округление значения до целого числа.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'При слиянии образовались новые клетки. Их {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клеток стало меньше: {sub} ' if sub > 0 else 'Клеток больше нет...'

    def __mul__(self, other):
        mul = self.quantity * other.quantity
        return f'Размножение клеток произошло успешно, теперь их {mul}'

    def __truediv__(self, other):
        truedly = self.quantity // other.quantity
        return f'Произошло деление, клеток {truedly} '


cell = Cell(32)
cell_2 = Cell(16)
print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)
