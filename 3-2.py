seasons = ['winter', 'spring', 'summer', 'autumn']
month = int(input("Введите, пожалуйста, номер месяца."))
if month ==1 or month == 12 or month == 2:
        print(seasons[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons[3])
else:
        print("Введен месяц, которого не существует")