#Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_numbers = []
with open('numbers.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_numbers.append(dic[i[0]] + '  ' + i[1])
    print(new_numbers)

with open('new_numbers.txt', 'w') as f_2:
    f_2.writelines(new_numbers)