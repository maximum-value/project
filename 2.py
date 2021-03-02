class MyException(Exception):

    def division_null(self, a, b):
        try:
            res = round(a/b, 2)
        except ZeroDivisionError:
            print(f"{a}/{b} -> На нуль делить нельзя\n")
        else:
            print(f"{a}/{b} = {res}\n")


m_e = MyException()

m_e.division_null(0, 1)
m_e.division_null(1, 0)
m_e.division_null(1, 2)
m_e.division_null(-1, 2)