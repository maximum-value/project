# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

with open("text.txt", "w") as f:
        line = input('Введите текст \n')
        while line:
                f.writelines(line)
                line = input('Введите текст \n')
                if not line:
                        break

with open("text.txt", "r") as f:
        content = f.readlines()
        print(content)


