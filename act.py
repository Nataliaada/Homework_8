import sqlite3

import Students as ST

connection = ST.create_connection("phyton1.db")


def option():
    print("\nВас приветствует программа по работе с БД студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть успеваемость \n \
    3: Добавить студента\n \
    4: Удалить студента\n \
    5: Редактировать запись \n \
    6: Вывести весь список студентов \n \
    Ваш выбор: '))

    if ch == 1:
        st = str(input("Введите фамилию ученика: "))
        select_by_name = "SELECT name, id FROM Student Where name LIKE \"" + st + "\""
        print(ST.execute_read_query(connection, select_by_name))
        exit()
    elif ch == 2:
        st = str(input("Введите телефон: "))
        select_by_name = "SELECT telephon, name , sourname FROM Student Where telephon LIKE \"" + st + "\""
        print(ST.execute_read_query(connection, select_by_name))
        exit()
    elif ch == 3:
        user_input = input("Введите по примеру: 1, 'Ivanov', 'Oleg','Petovich', '1982-06-15', 'male', 5464373")
        sqlite_insert_query = """INSERT INTO Student
                                         (id, sourname, name, secondname,  dateofbirth, gender, telephon)
                                         VALUES (""" + user_input + """);"""

        ST.execute_query(connection, sqlite_insert_query)
    elif ch == 4:
         st = input('Введите id ученика, которого нужно удалить из базы')
         print(ST.delete_sqlite_record(connection, st))

    elif ch == 5:
        st = input('Введите id ученика, которому нужно исправить номер телефона ')
        new = input('Введите новый номер телефон  ')
        update_query = "UPDATE   Student   SET  telephon = \"" + new + "\"   WHERE   id = \"" + st + "\""
        ST.update_sqlite_table(connection, update_query)
    elif ch == 6:

        select_student = "SELECT * from Student"
        users = ST.execute_read_query(connection, select_student)
        for student in users:
            print(student)
    else:
        print('еще раз')
    exit()


option()
