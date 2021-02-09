#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
name = input('Введите свое имя')
surname = input('Введите свою фамилию')
age = input('Введите год Вашего рождения')
city = input('Введите город проживания')
email = input('Введите Ващ e-mail')
phone = input('Введите Ваш номер телефона')
def my_func (name, surname, age, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(name = name, surname = surname,  age = age, city = city, email = email, telephone = phone))