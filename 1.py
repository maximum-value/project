class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date_1 = cls(day, month, year)
        print(cls, date_str)
        return date_1

    @staticmethod
    def date_real(date_str):
        day, month, year = map(int, date_str.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 9999:
            print(date_str)
            return day, month, year
        else:
            print('Данные введены некорректно')


d = '18-10-1983'
date2 = Date.from_str(d)
is_date = Date.date_real(d)