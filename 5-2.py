num = int(input("Введите число: "))
ml = [7, 4, 3, 2]
a = ml.count(num)
for element in ml:
    if a > 0:
        i = ml.index(num)
        ml.insert(i+c, num)
        break
    else:
        if num > element:
            j = ml.index(element)
            ml.insert(j, num)
            break
        elif num < ml[len(ml) - 1]:
            ml.append(num)
print(ml)
