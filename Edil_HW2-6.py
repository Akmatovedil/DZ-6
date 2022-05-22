import re

while 1:
    menu = int(input('Введите число от 1 до 5 для вывода следующей информации:\n'
                     ' 1 - Считать имена и фамилии,\n'
                     ' 2 - Считать все емайлы,\n'
                     ' 3 - Считать названия файлов,\n'
                     ' 4 - Считать цвета,\n'
                     ' 5 - Выход\n'))
    if menu == 4:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content = file.read()
            colors = re.findall(r'#[0-9a-zа-я]{6}', content)
            file = open('Colors.txt', 'w')
            file.write(f'{colors}')
            file.close()
    elif menu == 1:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content = file.read()
            name_surname = re.findall(r'[A-Za-z][^а-я][^0-9][^\\][^@][^\.]', content)
            file = open('name.txt', 'w')
            file.write(f'{name_surname}')
            file.close()

    elif menu == 5:
        print(f'Выход')
        break