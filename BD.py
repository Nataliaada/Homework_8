
import sqlite3



try:   #Создать таблицу
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    sqlite_create_table_query = '''CREATE TABLE sqlitedb_developers (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email text NOT NULL UNIQUE,
                                joining_date datetime,
                                salary REAL NOT NULL);'''

    sqlite_create_table_Student = '''CREATE TABLE Student (
         id INTEGER PRIMARY KEY,
         name surname TEXT NOT NULL,
         dateofbirth INTEGER,
         gender TEXT,
         id_lesson INTEGER NOT NULL,
         id_mark INTEGER NOT NULL,
         FOREIGN KEY (id_lesson) REFERENCES lessons (id),
         FOREIGN KEY (id_mark) REFERENCES marks (id)
         );'''

    create_lessons_table = """    CREATE TABLE IF NOT EXISTS lessons(
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL
                                            ); """
    create_marks_table = """ CREATE TABLE IF NOT EXISTS marks (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL
             ); """
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    cursor.execute(sqlite_create_table_Student)
    cursor.execute(create_lessons_table)
    cursor.execute(create_marks_table)
    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")





def insert_multiple_records(records,sqlite_insert_query):        #Добавить элементы в таблицы
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")



        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    # finally:
    #     if sqlite_connection:
    #         sqlite_connection.close()
    #         print("Соединение с SQLite закрыто")

sqlite_insert_query = """INSERT INTO sqlitedb_developers
                                 (id, name, email, joining_date, salary)
                                 VALUES (?, ?, ?, ?, ?);"""
records_to_insert = [(4, 'Jaroslav', 'idebylos@gmail.com', '2020-11-14', 8500),
                     (5, 'Timofei', 'ullegyddomm@gmail.com', '2020-11-15',6600),
                     (6, 'Novil', 'so@gmail.com', '2020-11-27', 7400),
                     (7, 'Nikita', 'aqillysso@gmail.com', '2020-11-27', 7400)]

insert_multiple_records(records_to_insert,sqlite_insert_query)

sqlite_insert_query = """INSERT INTO Student
                                 (id, name, dateofbirth, gender, id_lesson, id_mark)
                                 VALUES (?, ?, ?, ?, ?,?);"""
records_to_insert = [(1, 'Fedorov Jaroslav', '2020-11-14','male', 1,2),
                      (2, 'Los Timofei',  '2020-11-15','male',1,2),
                     (3, 'Menaev Novil',  '2020-11-27','male', 1,2),
                     (4, 'Ivanov Nikita', '2020-11-27', 'male',1,2)]

insert_multiple_records(records_to_insert,sqlite_insert_query)


sqlite_insert_query = """INSERT INTO lessons
                                 (id, title)
                                 VALUES (?, ?);"""
records_to_insert = [(1, 'Информатика'),
                     (2, 'Проектирование'),
                     (3, 'Дизайн'),
                     (4, 'Продвижение')]

insert_multiple_records(records_to_insert,sqlite_insert_query)


sqlite_insert_query = """INSERT INTO marks
                                 (id, name)
                                 VALUES (?, ?);"""
records_to_insert = [(1, 'Отлично'),
                     (2, 'Хорошо'),
                     (3, 'Удовлетворительно'),
                     (4, 'Неуд')]

insert_multiple_records(records_to_insert,sqlite_insert_query)


# def read_sqlite_table(records):
#     records= cursor.fetchall()
#     try:
#         sqlite_connection = sqlite3.connect('sqlite_python.db')
#         cursor = sqlite_connection.cursor()
#         print("Подключен к SQLite")
#
#         sqlite_select_query = """SELECT * from sqlitedb_developers"""
#         cursor.execute(sqlite_select_query)
#         records = cursor.fetchall()
#         print("Всего строк:  ", len(records))
#         print("Вывод каждой строки")
#         for row in records:
#             print("ID:", row[0])
#             print("Имя:", row[1])
#             print("Почта:", row[2])
#             print("Добавлен:", row[3])
#             print("Зарплата:", row[4], end="\n\n")
#
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
#     finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
#
# read_sqlite_table()




def update_sqlite_table(sql_update_query):   # Обновление/редактирование одной записи в таблице
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")


        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

update_query = """Update sqlitedb_developers set salary = 8000 where id = 4"""   #как сделать запрос и  ввести это с клаиватуры (как input())?
update_sqlite_table(update_query)

def delete_sqlite_record(dev_id):   #удаление записей
        try:
            sqlite_connection = sqlite3.connect('sqlite_python.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sql_update_query = """DELETE from sqlitedb_developers where id = ?"""
            cursor.execute(sql_update_query, (dev_id,))
            sqlite_connection.commit()
            print("Запись успешно удалена")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
# id = int(input('введите номер Id, котрый нужно удлалить из таблицы'))
# delete_sqlite_record(id)



