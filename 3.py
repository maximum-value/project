#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("staf_table.txt", "r") as file:
    workers = []
    value = []
    ml = file.read().split('\n')
    for i in ml:
        i = i.split()
        if int(i[1]) < 20000:
            value.append(i[0])
        workers.append(i[1])
print(f'Оклад меньше 20.000 {value}, средний оклад {sum(map(int, workers)) / len(workers)}')
