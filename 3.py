class Error:
    def __init__(self, *args):
        self.ml = []

    def my_input(self):
        while True:
            try:
                value = int(input('Пожалуйста, введите числовое значение и нажмите Enter '))
                self.ml.append(value)
                print(f'Текущий список - {self.ml}\n ')
            except:
                print(f"Вы ввели некорректное значение.")
                choice = input(f'Желаете попробовать еще раз? Y/N ')

                if choice == 'Y' or choice == 'y':
                    print(try_except.my_input())
                elif choice == 'N' or choice == 'n':
                    return f'Вы прервали программу'
                else:
                    return f'Вы прервали программу'


try_except = Error(1)
print(try_except.my_input())