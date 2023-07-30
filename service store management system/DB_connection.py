# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 27/07/2023
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


# User-defined function to perform various query operations
def query_execute(case, query, values):
    global_cursor.execute(query, values)
    # Case 1 and case 2  for insert and for update respectively
    if case == 1 or case == 2:
        connection.commit()
    # Case 3 for select which return single row from DB
    elif case == 3:
        result = global_cursor.fetchone()
        return result
    # Case 4 for select which returns multiple rows from DB
    elif case == 4:
        result = global_cursor.fetchall()
        return result
