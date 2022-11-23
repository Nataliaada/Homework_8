import sqlite3
from sqlite3 import Error


def create_conection(path):
    sqlite_connection = None
    try:
        sqlite_connection = sqlite3.connect(path)
        print("База данных создана и успешно подключена к SQLite")


    except Error as error:
        print("Ошибка при подключении к sqlite")
    return sqlite_connection

#
# sqlite_connection = sqlite3.connect('phyton1.db')  # Подключились к  базе SQLite


def execute_query(sqlite_connection, query): # Создать таблицу
    cursor = sqlite_connection.cursor()
    try:
        cursor.execute(query)
        sqlite_connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
# try:
#     create_lessons_table = """    CREATE TABLE IF NOT EXISTS lessons(
#                            id INTEGER PRIMARY KEY AUTOINCREMENT,
#                            title TEXT NOT NULL
#                                             ); """
#     execute_query(sqlite_connection, create_lessons_table)
#
# except sqlite3.Error as error:
#     print("Ошибка при подключении к sqlite", error)
# finally:
#     if (sqlite_connection):
#         sqlite_connection.close()
#         print("Соединение с SQLite закрыто")


def insert_multiple_records(records, sqlite_insert_query):  # Добавить элементы в таблицы
        sqlite_connection = sqlite3.connect('phyton1.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

#
#
# try:
#     sqlite_insert_query = """INSERT INTO lessons
#                                       (id, title)
#                                       VALUES (?, ?);"""
#     records_to_insert = [(1, 'Программирование'),
#                          (2, 'Разработка'),
#                          (3, 'Дизайн'),
#                          (4, 'Стратегический менеджмент')]
#
#     insert_multiple_records(records_to_insert, sqlite_insert_query)
#
# except sqlite3.Error as error:
#         print("Ошибка при работе с SQLite", error)
# finally:
#         if sqlite_connection:
#             sqlite_connection.close()
#             print("Соединение с SQLite закрыто")
#
#

def update_sqlite_table(sql_update_query):  # Обновление/редактирование одной записи в таблице
    try:
        sqlite_connection = sqlite3.connect('python.db')
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


# update_query = """Update Lessons set title = 'Технология дизайна' where id = 3"""  # как сделать запрос и  ввести это с клаиватуры (как input())?
# update_sqlite_table(update_query)


def delete_sqlite_record(dev_id):  # удаление записей
    try:
        sqlite_connection = sqlite3.connect('python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """DELETE from Lessons where id = ?"""
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
#
#

def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from Lessons"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("ID:", row[0])
            print("Наименование предмета:", row[1])

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


#
# print(read_sqlite_table())


