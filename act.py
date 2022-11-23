import BD

def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть успеваемость студент \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        name = str(input("Введите фамилию ученика: "))
        if name in BD.sqlite_create_table_Student['name']:
                index = BD.sqlite_create_table_Student['name'].index(name)
        print(f"{BD.sqlite_create_table_Student['ID'][index]}, {BD.sqlite_create_table_Student['name'][index]},{BD.sqlite_create_table_Student['dateofbirth'][index]}, {BD.sqlite_create_table_Student['id_lesson'][index]}, {BD.sqlite_create_table_Student['id_mark'][index]}")
        exit()

    elif ch == 2:
        c = input('Введите ID оценки: ')
        if c in BD.sqlite_create_table_Student['id_mark']:
            index = BD.sqlite_create_table_Student['id_mark'].index(c)
            print(
                f"{BD.sqlite_create_table_Student['ID'][index]}, {BD.sqlite_create_table_Student['name'][index]},"
                f"{BD.sqlite_create_table_Student['dateofbirth'][index]}, {BD.sqlite_create_table_Student['id_lesson'][index]}, "
                f"{BD.sqlite_create_table_Student['id_mark'][index]}")
    else:
        print('еще раз')
    exit()


option()