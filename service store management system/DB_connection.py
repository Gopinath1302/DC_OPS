# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 08/07/2023
# Reviewed by        : Silpa M
# Reviewed on        : 20/02/2023


import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="appdata"
)

global_cursor = connection.cursor()


def query_execute(case, query, values):
    global_cursor.execute(query, values)
    # for insert
    if case == 1:
        connection.commit()
    # for update
    elif case == 2:
        connection.commit()
    # for select
    elif case == 3:
        result = global_cursor.fetchone()
        return result
    # for select multiple rows
    elif case == 4:
        result = global_cursor.fetchall()
        return result
