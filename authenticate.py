from server import db,cursor
from books import bookS
import getpass
import re


class auth():
    @staticmethod
    def authenticate_user(username, password):
        
        query = "SELECT * FROM logindetails WHERE username = %s AND paasword = %s"
        cursor.execute(query, (username, password))

        result = cursor.fetchone()

        return result is not None

    @staticmethod
    def login():
        entered_username = input("Enter your username: ")
        entered_password = getpass.getpass("Enter your password: ")
        if auth.authenticate_user(entered_username, entered_password):
            print("Login successful. Proceed with further actions.")
            object1 = bookS()
            object1.book_details()
        else:
            print("Invalid username or password. Login failed. \n")
            print(" Enter 1 for Login again \n Enter 2 for Register \n Enter 3 for logout")
            opt=int(input())
            if opt==1:
             auth.login()
            elif opt==2:
             Register.getin()
            else:
               print("Logout")

class Register(auth):
    @staticmethod
    def register_user(username, password, name, phonenumber):
        
        query = "INSERT INTO logindetails (username, paasword, name,number) VALUES (%s, %s, %s, %s)"
        values = (username, password, name, phonenumber)
        cursor.execute(query, values)

        db.commit()


    @staticmethod
    def getin():
        flag = True
        regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
        check = re.compile(regex)
        while flag:
            username = input("Enter the Username:\n")
            query = "Select username from logindetails where username=%s"
            cursor.execute(query,(username,))
            result = cursor.fetchone()
            if re.search(check,username)  and result is None:
                flag = False
            else:
                print("Invalid Username! or \n User name already exist\nPlease try to enter a valid username!")
        regex = ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
        check = re.compile(regex)
        flag=True
        while flag:
            password = input("Enter the password:\n")
            if re.search(check, password):
                flag = False
            else:
                print("Invalid password!\nPlease try  to enter a valid password")
        name = input("Enter your Name: ")
        flag = True
        while flag:
            try:
                mobile = int(input("Enter your Mobile number:\n"))
            except:
                print("Invalid entry !\nPlease try  to enter a valid Mobile number")
            else:
                if 6000000000 < mobile < 10000000000:
                    flag = False
                else:
                    print("Invalid Mobile number!\nPlease try  to enter a valid Mobile number")
        Register.register_user(username, password, name, mobile)
        auth.login()
