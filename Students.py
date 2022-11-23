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


def execute_query(sqlite_connection, query):  # Создать таблицу
    cursor = sqlite_connection.cursor()
    try:
        cursor.execute(query)
        sqlite_connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# try:
#     sqlite_create_table_Student = '''CREATE TABLE Student (
#          id INTEGER PRIMARY KEY,
#          name surname TEXT NOT NULL,
#          dateofbirth INTEGER,
#          gender TEXT,
#          id_lesson INTEGER NOT NULL,
#          id_mark INTEGER NOT NULL,
#          FOREIGN KEY (id_lesson) REFERENCES lessons (id),
#          FOREIGN KEY (id_mark) REFERENCES marks (id)
#          );'''
#     execute_query(sqlite_connection, sqlite_create_table_Student)
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")


def insert_multiple_records(connection, records, sqlite_insert_query):  # Добавить элементы в таблицы
    cursor = connection.cursor()
    cursor.executemany(sqlite_insert_query, records)
    connection.commit()
    print("Записи успешно вставлены в таблицу Student", cursor.rowcount)
    connection.commit()
    cursor.close()


#
#
# try:
#      sqlite_insert_query = """INSERT INTO Student
#                                  (id, name, dateofbirth, gender, id_lesson, id_mark)
#                                  VALUES (?, ?, ?, ?, ?,?);"""
#      records_to_insert = [(5, 'Ivanov Oleg', '1982-06-27', 'male', 1, 2),
#                           (6, 'Mironov Nikita', '1982-07-27', 'male', 1, 2),
#                           (7, 'Onishuk Nikonor', '1983-02-27', 'male', 1, 2)]
#
#      insert_multiple_records(records_to_insert, sqlite_insert_query)

# sqlite_insert_query = """INSERT INTO Student
#                                  (id, name, dateofbirth, gender, id_lesson, id_mark)
#                                  VALUES (?, ?, ?, ?, ?,?);"""
# records = [(1, 'Ivanov Oleg', '1982-06-15', 'male', 1, 2),
#            (2, 'Petrov Igot', '1982-01-27', 'male', 1, 2),
#            (3, 'Smirnov Igot', '1982-07-22', 'male', 1, 2),
#            (4, 'Egorov Anton', '1982-06-27', 'male', 1, 2),
#            (5, 'Petrov Anton', '1982-03-18', 'male', 1, 2),
#            (6, 'Sergeev Sergey', '1982-02-02', 'male', 1, 2),
#            (7, 'Ragin Evhenii', '1983-02-04', 'male', 1, 2)]
#insert_multiple_records(records, sqlite_insert_query)
# except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
# finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
#
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

#
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

#
# select_student = "SELECT * from Student"
# users = execute_read_query(sqlite_connection, select_student)
# #
# for student in users:
#      print(student)
