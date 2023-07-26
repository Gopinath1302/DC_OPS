import sys
import datetime

import mysql
from user.user import User, AdminUser
from db.db_connector import get_db_connection


class Welcome:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.create_timestamp_login_table_if_not_exists()

    def create_timestamp_login_table_if_not_exists(self):
        cursor = self.db_connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS timestamp_login (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME NOT NULL
        )
        """
        try:
            cursor.execute(query)
            self.db_connection.commit()
        except mysql.connector.Error as err:
            print("Error creating table: {}".format(err))
        finally:
            cursor.close()

    def record_login_timestamp(self):
        timestamp = datetime.datetime.now()
        cursor = self.db_connection.cursor()
        query = "INSERT INTO timestamp_login (timestamp) VALUES (%s)"
        values = (timestamp,)
        try:
            cursor.execute(query, values)
            self.db_connection.commit()
        except mysql.connector.Error as err:
            print("Error inserting timestamp: {}".format(err))
        finally:
            cursor.close()

    def show_login_choices(self):
        welcome = Welcome()
        welcome.record_login_timestamp()

        print("Welcome to Adam's Pet Shop!")
        print("Please choose:")
        print("1. Admin Login")
        print("2. Customer Login")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            from user.user import AdminUser

            admin_user = AdminUser()
            admin_user.admin_login()

        elif choice == "2":
            from user.user import User

            user = User()
            user.customer_login()

        else:
            print("Invalid choice. Please enter either '1' or '2'.")
            sys.exit(1)
