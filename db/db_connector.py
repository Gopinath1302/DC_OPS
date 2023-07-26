# db_connector.py

import mysql.connector


def get_db_connection():
    db_connection = mysql.connector.connect(
        host="127.0.0.15",
        user="root",
        password="root",
        database="pet_adoption",
    )
    return db_connection
