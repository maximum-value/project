#Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.

subjects = {}
with open('school.txt', 'r') as f:
    for line in f:
        sub, lec, pr, lab = line.split()
        subjects[sub] = int(lec) + int(pr) + int(lab)
    print(f'Общее количество часов по предмету - \n {subjects}')