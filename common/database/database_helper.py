import psycopg2

from database.db_connections import postgre_connection


def execute_select_query(select_query: str) -> []:
    """
    Execute select query in POSTGRE
    :param select_query:
    :param connection: postgre connection
    :return: Mảng các giá trị dict hoặc []
    """
    connection = postgre_connection()
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(select_query)
        cols_description = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        for row in rows:
            data = {}  # dữ liệu của một bản ghi
            for index, value in enumerate(row):
                data[cols_description[index]] = value
            result.append(data)
    except (Exception, psycopg2.Error) as error:
        print("execute_select_query error", error)
        connection.rollback()
        cursor.close()
        connection.close()

    return result