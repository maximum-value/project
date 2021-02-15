#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("text_file.txt", "r") as file:
    content = file.readlines()
    print(f'Количество строк в файле - {len(content)}')
    for i in range(len(content)):
        print(f'Количество символов {i + 1} - ой строки {len(content[i])}')