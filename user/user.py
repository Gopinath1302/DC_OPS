import mysql.connector
from db.db_connector import get_db_connection


class AdminUser:
    def __init__(self):
        self.db_connection = get_db_connection()
        cursor = self.db_connection.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS admin_users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(50)
        )
        """
        cursor.execute(query)
        self.db_connection.commit()

    def admin_login(self):
        # Implement logic for admin login
        print("Admin Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        cursor = self.db_connection.cursor()
        query = "SELECT * FROM admin_users WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        admin_user = cursor.fetchone()
        cursor.close()

        if admin_user:
            print("Admin login successful!")
            return True
        else:
            print("Invalid username or password for admin login.")
            return False


class User:
    def __init__(self):
        self.db_connection = get_db_connection()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        cursor = self.db_connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(50)
        )
        """
        cursor.execute(query)
        self.db_connection.commit()
        cursor.close()

    def create_account(self):
        # Implement logic to create a user account and store the credentials in the database
        print("Create a new user account:")
        username = input("Enter a username: ")
        password = input("Enter a password: ")

        cursor = self.db_connection.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)
        self.db_connection.commit()
        cursor.close()

        print("Account created successfully!")

    def customer_login(self):
        # Implement logic for customer login or account creation
        print("Welcome to Adam's Pet Shop!")
        print("Please choose:")
        print("1. Account Login")
        print("2. Account Creation")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("Customer Login:")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            cursor = self.db_connection.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            values = (username, password)
            cursor.execute(query, values)
            user = cursor.fetchone()
            cursor.close()

            if user:
                print("Customer login successful!")
                return True
            else:
                print("Invalid username or password for customer login.")
                return False
        elif choice == "2":
            self.create_account()
            return self.customer_login()
        else:
            print("Invalid choice. Please enter either '1' or '2'.")
            return False
