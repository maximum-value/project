# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента

my_list = [22, 44, 56, 11, 300, 9, 9, 15, 666, 777]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)