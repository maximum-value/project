class Warehouse:
    print("\nСклад оргтехники")


class Office:
    def __init__(self, manufacturer, color):
        self.manufacturer = manufacturer
        self.color = color


class Printer(Office):
    amount_p = 0

    def __init__(self, manufacturer, color, type):
        super().__init__(manufacturer, color)
        self.type = type
        Printer.amount_p += 1

    @staticmethod
    def name():
        return "<<Принтер>>"

    def type_printer(self):
        return self.type

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tтип принтера: {}".format(self.manufacturer, self.color, self.type)


class Scanner(Office):
    amount_sc = 0

    def __init__(self, manufacturer, color, sensor):
        super().__init__(manufacturer, color)
        self.sensor = sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return"<<Сканер>>"

    def type_sensor(self):
        return self.sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tсенсор: {}".format(self.manufacturer, self.color, self.sensor)


class Xerox(Office):
    amount_x = 0

    def __init__(self, manufacturer, color, xer):
        super().__init__(manufacturer, color)
        self.xer = xer
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "<<Ксерокс>>"

    def wi_fi_module(self):
        return self.xer

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi модуль: {}".format(self.manufacturer, self.color, self.xer)


p = Printer('HP', 'black', 'лазерный')
p2 = Printer('Smart Tank', 'white', 'лазерный')
print(p.name(), p.amount_p, "шт")
print(p.__str__())
print(p2.__str__())


s = Scanner('HP', 'black', 'CIS')
s2 = Scanner('Smart Tank', 'white', 'CCD')
s3 = Scanner('HP', 'white', 'CCD')
print(s.name(), s.amount_sc, "единиц товара")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())


x = Xerox('HP', 'black', 'отсутствует')
x2 = Xerox('HP', 'white', 'есть')
x3 = Xerox('Xerox', 'white', 'есть')
x4 = Xerox('Xerox', 'black', 'отсутствует')
print(x.name(), x.amount_x, "единиц товара")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
print(x4.__str__())
