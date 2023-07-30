# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 27/07/2023
# Reviewed by        : Silpa M
# Reviewed on        : 20/02/2023


import re
from DB_connection import global_cursor, query_execute
from datetime import date, datetime
import hashlib
# from pwinput import pwinput


class User:
    __customer_id: str = "1"
    __username: str = "sf"
    __password: str = "fs"
    __phone: int = 0
    __email_id: str = ""
    __address: str = ""
    __first_name: str = ""
    __last_name: str = ""
    __DOB = ""
    user_choice: int = 0

    # Function to
    @staticmethod
    def get_timestamp(case=0):
        # Get the current timestamp
        timestamp = datetime.timestamp(datetime.now())
        # gets current date
        value = date.today()
        # Format the datetime object as a string
        dt = datetime.fromtimestamp(timestamp)
        # Format the datetime object as a string
        formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
        #
        current_time = datetime.now().time()
        time_string = current_time.strftime("%I:%M:%S %p")
        # function call for timestamp
        if case == 1:
            return timestamp
        # function call for date and time
        elif case == 2:
            return formatted_datetime
        # function call for date
        elif case == 3:
            return value
        # function call for time with local format
        elif case == 4:
            return time_string

    # Function to convert password into a hash value
    @staticmethod
    def generate_sha256_hash(value):
        sha256_hash = hashlib.sha256(value.encode()).hexdigest()
        return sha256_hash

    # User-defined function to get user's choice
    @staticmethod
    def get_user_choice(prompt, valid_choices):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input in valid_choices:
                    return user_input
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # User-defined function to generate Customer_id
    @staticmethod
    def generate_customer_id(username="", phone=""):
        username = re.sub(r"\s+", " ", username)
        username = username.upper()
        cus_id = "CUS" + username[:2] + phone[:5]
        return cus_id

    # User-defined function to print User details
    @classmethod
    def print_user_details(cls, __customer_id=""):
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t- > Details < -")
        print("_" * 100, "\n")
        query = "Select * from userdata where cus_id = %s;"
        values = (__customer_id,)
        result = query_execute(3, query, values)
        print("Customer ID:", result[0], "\t\t\t", "Username:", result[1])
        print("First Name:", result[2], "\t\t\t", "Last Name:", result[3])
        print("Date of Birth:", result[4], "\t\t  ", "Email ID:", result[5])
        print("Mobile Number:", result[6])
        query = "Select * from address where cus_id = %s;"
        values = (__customer_id,)
        result = query_execute(3, query, values)
        value = result[1:7]
        for i in range(len(value)):
            if i < 1:
                print("Address:", value[i], ",")
            else:
                print("\t\t", value[i], ",")
            if i == len(value) - 1:
                print("\t\t", value[i], ".")
        # pass

    # User-defined function to update User details
    @classmethod
    def update_user_details(cls, __customer_id=""):
        global __username, __email_id, __phone, __first_name, __last_name, __DOB, user_choice, __address
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t- > Updation < -")
        print("_" * 100, "\n")
        prompt = "Which details do you need to update \n1.First name,\n2.Last name,\n3.Date of Birth," \
                 "\n4.Address\n5.Update all details\n6.Back to dashboard\n"
        valid_choices = [1, 2, 3, 4, 5, 6]
        while True:
            user_choice = User.get_user_choice(prompt, valid_choices)
            if user_choice == 1:
                print("Enter the your First name:")
                __first_name = input()
                query = "update userdata set fname=%s, timestamp=%s where cus_id=%s;"
                timestamp = User.get_timestamp(2)
                values = (__first_name, timestamp, __customer_id)
                query_execute(2, query, values)
                print("\n", "-" * 25, ">Successfully updated the User Information<", "-" * 25, "\n")
            elif user_choice == 2:
                print("Enter the your Last name:")
                __last_name = input()
                query = "update userdata set lname=%s, timestamp=%s where cus_id=%s;"
                timestamp = User.get_timestamp(2)
                values = (__last_name, timestamp, __customer_id)
                query_execute(2, query, values)
                print("\n", "-" * 25, ">Successfully updated the User Information<", "-" * 25, "\n")
            elif user_choice == 3:
                print("Enter the Your Date of Birth (YYYY-MM-DD):")
                __DOB = input()
                query = "update userdata set dob=%s, timestamp =%s where cus_id=%s;"
                timestamp = User.get_timestamp(2)
                values = (__DOB, timestamp, __customer_id)
                query_execute(2, query, values)
                print("\n", "-" * 25, ">Successfully updated the User Information<", "-" * 25, "\n")
            elif user_choice == 4:
                print("Enter the Your address:")
                print("Door no:")
                door_no = input()
                print("Street name:")
                street = input()
                print("City:")
                city = input()
                print("State:")
                state = input()
                print("Pin code/ Postal code:")
                zip_code = input()
                print("Country:")
                country = input()
                query = "update address set door_no=%s, street=%s, city=%s, state=%s, country=%s, zip_code=%s, timestamp =%s where cus_id =%s;"
                timestamp = User.get_timestamp(2)
                values = (door_no, street, city, state, country, zip_code, timestamp, __customer_id)
                query_execute(2, query, values)
                print("\n", "-" * 25, ">Successfully updated the User Information<", "-" * 25, "\n")
            elif user_choice == 5:
                print("Enter the your First name:")
                __first_name = input()
                print("Enter the your Last name:")
                __last_name = input()
                print("Enter the Your Date of Birth (YYYY-MM-DD):")
                __DOB = input()
                query = "update userdata set fname=%s, lname=%s, dob=%s, timestamp=%s where cus_id=%s;"
                timestamp = User.get_timestamp(2)
                values = (__first_name, __last_name, __DOB, timestamp, __customer_id)
                query_execute(2, query, values)
                print("Enter the Your address:")
                print("Door no:")
                door_no = input()
                print("Street name:")
                street = input()
                print("City:")
                city = input()
                print("State:")
                state = input()
                print("Pin code/ Postal code:")
                zip_code = input()
                print("Country:")
                country = input()
                # cus_id, door_no, street, city, state, country, zip_code, timestamp
                query = "update address set door_no=%s, street=%s, city=%s, state=%s, country=%s, zip_code=%s, timestamp =%s where cus_id =%s;"
                timestamp = User.get_timestamp(2)
                values = (door_no, street, city, state, country, zip_code, timestamp, __customer_id)
                query_execute(2, query, values)
                print("\n", "-" * 25, ">Successfully updated the User Information<", "-" * 25, "\n")
            elif user_choice == 6:
                break

    # User-defined function to authenticate the user
    @classmethod
    def sign_in(cls):
        if global_cursor is None:
            raise Exception("Cursor not initialized. Call create_cursor() first.")
        global user_choice, __username, __password, __email_id, __phone, __customer_id
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t- > Sign-in < -")
        print("_" * 100, "\n")
        flag = True
        prompt = ("\n\t\t\t\t\tError!, invalid credentials\nWant retry to signing-in ? or "
                  "exit the"
                  "application.\n\t 1.Sign-in\t2.Exit\n")
        valid_choice = [1, 2]
        while flag:
            print("Enter your username:")
            __username = input()
            print("Enter your password:")
            __password = input()
            query = "Select * from credentials where username=%s;"
            hash_value = User.generate_sha256_hash(__password)
            global_cursor.execute(query, (__username,))
            result = global_cursor.fetchone()
            # print(1)
            try:
                __customer_id = result[0]
                credentials = result[2]
                # print(2)

            except:
                # print(3)
                user_choice = User.get_user_choice(prompt, valid_choice)
                if user_choice == 1:
                    flag = True
                elif user_choice == 2:
                    flag = False
                    quit()
            else:
                if credentials == hash_value:
                    print("\n\t\t\t\t\tlogged-in successfully!\n")
                    return __customer_id
                else:
                    user_choice = User.get_user_choice(prompt, valid_choice)
                    if user_choice == 1:
                        flag = True
                    elif user_choice == 2:
                        flag = False
                        quit()

    # User-defined function to validate an existing user
    @staticmethod
    def check_existing_user(value="", case=0):
        result = ""
        values = (value,)
        if case == 1:
            query = "Select username from credentials where username=%s;"
            result = query_execute(3, query, values)
        elif case == 2:
            query = "Select username from credentials where phoneno=%s;"
            result = query_execute(3, query, values)
        elif case == 3:
            query = "Select username from credentials where emailid=%s;"
            result = query_execute(3, query, values)
        return result is not None

    # User-defined function to validate username
    @staticmethod
    def username_validation(username):
        regex = "(?=.*[a-z])(?=.*[A-Z]).+$"
        rule = re.compile(regex)
        if re.search(rule, username):
            result = User.check_existing_user(username, 1)
            if result:
                print("This username is already exist")
                prompt = " 1.Try to enter another username or 2.try log in with that username ?\n"
                valid_choice = [1, 2]
                user_choices = User.get_user_choice(prompt, valid_choice)
                if user_choices == 2:
                    User.sign_in()
                else:
                    return True
            else:
                return False
        else:
            return True

    # User-defined function to validate password
    @staticmethod
    def password_validation(password):
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        rule = re.compile(regex)
        if re.search(rule, password):
            return True
        else:
            return False

    # User-defined function to validate mobile number
    @staticmethod
    def phone_no_validation(phone):
        if 6000000000 < phone < 10000000000:
            result = User.check_existing_user(str(phone), 2)
            if result:
                print(
                    "This phone number is already link with another account\n\t Try to enter another number...")
                return True
            else:
                return False

    # User-defined function to validate email-id
    @staticmethod
    def email_id_validation(email_id):
        regex = "^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        rule = re.compile(regex)
        if re.search(rule, email_id):
            result = User.check_existing_user(email_id, 3)
            if result:
                print("This email id is already link with another account")
                prompt = " 1.Try to enter another email id or 2.try log in with that email ?"
                valid_choice = [1, 2]
                user_choices = User.get_user_choice(prompt, valid_choice)
                if user_choices == 2:
                    User.sign_in()
                else:
                    return True
            else:
                return False
        else:
            return True

    # User-defined function to create a user
    @classmethod
    def sign_up(cls):
        global __customer_id, user_choice, __username, __password, __email_id, __phone
        print("_" * 100, "\n\t\t\t\t\t\t\t\t\t- > Sign-Up < -"),
        print("_" * 100, "\n")
        flag = True
        # regex = "(?=.*[a-z])(?=.*[A-Z]).+$"
        # rule = re.compile(regex)
        while flag:
            __username = input("Enter the Username:\n")
            flag = User.username_validation(__username)
            if flag:
                print("Invalid Username!\nPlease try to enter a valid username!\n")
            else:
                flag = False
        flag = True

        while flag:
            __password = input("Enter the password:\n")
            flag = User.password_validation(__password)
            if flag:
                __password = User.generate_sha256_hash(__password)
                flag = False
            else:
                print("Invalid password!\nPlease try  to enter a valid password\n")
        flag = True

        while flag:
            try:
                __phone = int(input("Enter your Mobile number:\n"))
            except:
                print("Invalid entry !\nPlease try to enter a valid Mobile number\n")
            else:
                flag = User.phone_no_validation(__phone)
                if flag:
                    print("Invalid Mobile number!\nPlease try  to enter a valid Mobile number\n")
                else:
                    flag = False
        flag = True

        while flag:
            __email_id = input("Enter the email:\n")
            flag = User.email_id_validation(__email_id)
            if flag:
                flag = False
            else:
                print("Invalid Email Id!\nPlease try  to enter a valid email")

        # Uploading the user's details inside the database
        __customer_id = User.generate_customer_id(__username, str(__phone))
        date1 = User.get_timestamp(3)
        query = "insert into credentials values(%s,%s,%s,%s,%s,%s);"
        values = (__customer_id, __username, __password, str(__phone), __email_id, date1)
        query_execute(1, query, values)
        timestamp = User.get_timestamp(2)
        query = "insert into userdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (__customer_id, __username, None, None, None, __email_id, str(__phone), None, timestamp)
        query_execute(1, query, values)
        query = "insert into address values(%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (__customer_id, None, None, None, None, None, None, timestamp)
        query_execute(1, query, values)
        print("\n", "-" * 25, ">Successfully registered as the User<", "-" * 25)
        return __customer_id
