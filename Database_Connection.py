import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    password = 'Balaji@1302',
    user ='root',
    database='aspire_database'
    )

global_cursor = connection.cursor()
