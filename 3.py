# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(a, b, c):
    if a != b != c:
        z = [a, b, c]
        z.remove(min(a, b, c))
        return sum(z)
    else:
        return a + b
print(f'Result - {my_func(int(input("Введите первый аргумент ")), int(input("Введите второй аргумент ")), int(input("Введите третий аргумент ")))}')

