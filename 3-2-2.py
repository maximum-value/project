sdict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите, пожалуйста, номер месяца."))
if month ==1 or month == 12 or month == 2:
        print(sdict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(sdict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(sdict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(sdict.get(4))
else:
        print("Введен месяц, которого не существует")