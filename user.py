import Db_connection
from Db_connection import cursor,connect
import train
import datetime
import time
import re
def register(username, password):
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connect.commit()
        print("Registration successful!")
    except :
        print("Error: Username already exists.")
def login(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")
def main():
    print("...................Railway Management System................")
    flag = True
    while flag:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        # choice = int(input("Enter your choice: "))
        while True:
            try:
                choice = int(input("Enter a number: "))
                break  # Break out of the loop if a valid number is entered
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # time.sleep(5)
        if choice == 1:
            flag = True
            while flag:
                username_pattern = ("(?=.*[a-z])(?=.*[A-Z]).+$")
                username = input("Enter user name: ")
                if re.match(username_pattern, username):
                    print("Valid username!")
                    flag = False
                else:
                    print("Invalid username. Please try again.")
            flag = True
            while flag:
                password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"
                password = input("Enter password: ")
                if re.match(password_pattern, password):
                    print("Valid Password!")
                    flag = False
                else:
                    print("Invalid Password. Please try again.")
            register(username, password)
            flag = True
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
            train.main()
            # details_of_passengers.to_select()
        elif choice == 3:
            flag = False

        else:
            print("Invalid choice. Try again.")



