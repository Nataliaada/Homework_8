import sqlite3

import Lessons as L
import Students as ST
import Marks as M


connection = ST.create_connection("phyton1.db")


def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Поиск ID студента по фамилии \n \
    2: Посмотреть успеваемость \n \
    3: Добавить ученика\n \
    4: Удалить ученика\n \
    5: Редактировать запись \n \
    6: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        st = str(input("Введите фамилию ученика: "))
        select_by_name = "SELECT name, id FROM Student Where name LIKE \"" + st + "\""
        print(ST.execute_read_query(connection, select_by_name))
        exit()
    elif ch == 2:
        st = str(input("Введите id предмета: "))
        select_by_name = "SELECT id_lesson, id_mark FROM Student Where id_lesson LIKE \"" + st + "\""
        print(ST.execute_read_query(connection, select_by_name))
        exit()
    elif ch == 3:

        sqlite_insert_query = """INSERT INTO Student
                                         (id, name, dateofbirth, gender, id_lesson, id_mark)
                                         VALUES (?, ?, ?, ?, ?,?);"""
        records = input("Введите как в примере:(9, 'Иванов', '1982-05-07', 'male', 1, 2)")


        print(ST.insert_multiple_records(connection, records, sqlite_insert_query))
    elif ch == 4:
        st = input('Введите id ученика, которого нужно удалить из базы')
        dev_id = " DELETE from Student where id  LIKE \"" + st + "\""
        print(ST.delete_sqlite_record(connection, dev_id))

    elif ch == 5:
        st = input('Введите id ученика, которому нужно исправить оценку На 5 ')
        new =input('Введите id оценки на  которую нужно исправить оценку ')
        update_query = "UPDATE   Student   SET  id_mark LIKE \"" + new + "\"   WHERE   id LIKE \"" + st + "\""
        ST.update_sqlite_table(connection, update_query)

    else:
        print('еще раз')
    exit()

option()
