goods = []
i = 1
while True:
    goods.append(
        (input('Введите порядковый номер товара: '), dict({
            'название': str(input('Введите наименование товара: ')),
            'цена': float(input('Введите цену единицы товара: ')),
            'количество': int(input('Введите количество товара: ')),
            'eд': str(input('Введите единицы товара: ')),
        }))
    )

    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
        break

    i += 1

print(f'Перечень товаров:{goods}')

analitics= dict({})
for product in goods:
    for key, value in product[-1].items():
        if key in analitics:
            if value not in analitics.get(key):
                analitics.get(key).append(value)
        else:
            analitics.update({key: [value]})


print(f'Собранные данные проанализированы: {analitics}')