el_count = int(input("Введите количество элементов списка "))
ml = []
i = 0
el = 0
while i < el_count:
    ml.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(ml)/2)):
        ml[el], ml[el + 1] = ml [el + 1], ml[el]
        el += 2
print(ml)



