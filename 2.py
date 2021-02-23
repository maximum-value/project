# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, volume):
        self.volume = volume

    @property
    def cost(self):
        return f'Расход ткани равен - {self.volume / 6.5 + 0.5 + 2 * self.volume + 0.3 :.2f} см'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'

class Coat(Clothes):
    def cost(self):
        return f'Расход ткани на пальто - {self.volume / 6.5 + 0.5 :.2f}  см. ткани'

    def abstract(self):
        return 'Smth vary abstract second'

class Costume(Clothes):
    def cost(self):
        return f'Расход ткани на костюм {2 * self.volume + 0.3 :.2f} см. ткани'

    def abstract(self):
        pass

coat = Coat(42)
costume = Costume(168)
print(coat.cost)
print(costume.cost())
print(coat.abstract())