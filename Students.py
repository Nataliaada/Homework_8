import sqlite3
from sqlite3 import Error


def create_connection(path):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(path)
        print("База данных создана и успешно подключена к SQLite")
    except Error as error:
        print(f"Ошибка '{error}' при подключении к sqlite")
    return sqlite_connection


def execute_query(connection, query):  # Создать таблицу
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#
# try:
#     sqlite_create_table_Student = '''CREATE TABLE Student (
#          id INTEGER PRIMARY KEY,
#          sourname surname TEXT NOT NULL,
#          name surname TEXT NOT NULL,
#          secondname surname TEXT NOT NULL,
#          dateofbirth INTEGER,
#          gender TEXT,
#          telephon INTEGER NOT NULL
#          );'''
#     execute_query(connection, sqlite_create_table_Student)
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (connection):
#         connection.close()
#         print("Соединение с SQLite закрыто")
#

def insert_multiple_records(connection, records, sqlite_insert_query):  # Добавить элементы в таблицы
    cursor = connection.cursor()
    cursor.executemany(sqlite_insert_query, records)
    connection.commit()
    print("Записи успешно вставлены в таблицу Student", cursor.rowcount)
    connection.commit()
    cursor.close()


#
#
#
# try:
# #      sqlite_insert_query = """INSERT INTO Student
# #                                  (id, name, dateofbirth, gender, id_lesson, id_mark)
# #                                  VALUES (?, ?, ?, ?, ?,?);"""
# #      records_to_insert = [(5, 'Ivanov Oleg', '1982-06-27', 'male', 1, 2),
# #                           (6, 'Mironov Nikita', '1982-07-27', 'male', 1, 2),
# #                           (7, 'Onishuk Nikonor', '1983-02-27', 'male', 1, 2)]
# #
# #      insert_multiple_records(records_to_insert, sqlite_insert_query)

#   sqlite_insert_query = """INSERT INTO Student
#                                  (id, sourname, name, secondname,  dateofbirth, gender, telephon)
#                                  VALUES (?, ?, ?, ?, ?, ?, ?);"""
#   records = [(1, 'Ivanov', 'Oleg','Petovich', '1982-06-15', 'male', 5464373),
#            (2, 'Petrov', 'Igot', 'Ivanovich','1982-01-27', 'male', 4847763),
#            (3, 'Smirnov', 'Igot', 'Sergeevich', '1982-07-22', 'male', 3773173),
#            (4, 'Egorov', 'Anton', 'Sergeevich','1982-06-27', 'male', 3737373),
#            (5, 'Petrov', 'Anton','Andreevich', '1982-03-18', 'male', 1435465),
#            (6, 'Sergeev', 'Sergey','Sergeevich', '1982-02-02','male',6545464),
#            (7, 'Ragin', 'Evgenii','Olegovich', '1983-02-04', 'male', 6574635)]
#   insert_multiple_records(connection, records, sqlite_insert_query)
# except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
# finally:
#         if connection:
#             connection.close()
#             print("Соединение с SQLite закрыто")
#


def update_sqlite_table(connection, sql_update_query):  # Обновление/редактирование одной записи в таблице
    try:
        cursor = connection.cursor()
        cursor.execute(sql_update_query)
        connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# update_query = """Update Student set id_mark = 1 where id = 3"""  # как сделать запрос и  ввести это с клаиватуры (как input())?
# update_sqlite_table(update_query)
#

def delete_sqlite_record(connection, dev_id):  # удаление записей
    try:
        cursor = connection.cursor()
        sql_update_query = """DELETE from Student where id = ?"""
        cursor.execute(sql_update_query, (dev_id,))
        connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# id = int(input('введите номер Id, котрый нужно удлалить из таблицы'))
# delete_sqlite_record(id)


def read_sqlite_table(connection):
    try:
        connection = sqlite3.connect('python.db')
        cursor = connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from Student"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("ID:", row[0])
            print("ФИО:", row[1])
            print("Дата рождения:", row[2])
            print("Пол:", row[3])
            print("ID предмета:", row[4])
            print("ID оценки:", row[5])
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")


# print(read_sqlite_table())


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# select_student = "SELECT * from Student"
# users = execute_read_query(sqlite_connection, select_student)

# for student in users:
#      print(student)
