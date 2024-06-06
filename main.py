import mysql.connector
from config import host, user, password, db_name

def display_table(connection, table_name):
    """Отобразить содержимое таблицы."""
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    for row in cursor:
        print(row)


def delete_row(connection, table_name, column_value):
    """Удалить строку из таблицы по значению указанного столбца."""
    cursor = connection.cursor()
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    column_names = [column[0] for column in cursor]
    column_name = column_names[0]  
    
    sql = f'DELETE FROM {table_name} WHERE {column_name} = %s'
    cursor.execute(sql, (column_value,))
    connection.commit()
    
def display_column_names(connection, table_name):
    """Отобразить названия столбцов в таблице."""
    cursor = connection.cursor()
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    column_names = [column[0] for column in cursor]
    print("Столбцы:")
    print(' '.join(column_names))
    
def fill_table(connection, table_name):
    """Заполнить таблицу значениями пользователя."""
    # Получить названия столбцов
    cursor = connection.cursor()
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    column_names = [column[0] for column in cursor]

    # Заполнить таблицу значениями пользователя
    values = []
    for column_name in column_names:
        value = input(f"Введите значение для {column_name}: ")
        values.append(value)

    # Сформировать SQL-запрос для вставки новой строки
    sql = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(values))})"
    cursor.execute(sql, values)
    connection.commit()
    
def main():
    # Подключение к базе данных
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )


    # Отображение содержимого всех таблиц
    print("Все доступные таблицы:")
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table[0])

    # Выбор таблицы
    print("Выберите таблицу:")
    table_name = input()

    # Отображение названий столбцов
    display_column_names(connection, table_name)
    # Отображение содержимого таблицы
    display_table(connection, table_name)
    
    
    print("Что вы хотите сделать?")
    print("1. Удалить строку")
    print("2. Заполнить таблицу")
    print("3. Выход")
    choice = input()
    if choice == "1":
        print("Введите строку для удаления:")
        column_value = input()
        delete_row(connection, table_name, column_value)
        display_table(connection, table_name)
    if choice == "2":
        # Заполнение таблицы
        fill_table(connection, table_name)
        display_table(connection, table_name)
    if choice == "3":
        exit()
    
    connection.close()

if __name__ == "__main__":
    main()