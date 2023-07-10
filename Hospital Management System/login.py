import re
import mysql.connector
from authentication import access
from patient import Patient
from doctor import Doctor
passcheck= r'^[a-z to A-Z to 0-9]+[!@#$%^&*()_+]?\w{0,5}$'
class Login:
    def login_(profile):
        username = input("\nEnter your Username: ").lower()
        Password = input("Enter your password: ")
        if(profile==1):
            validate=access.verify(username,Password,profile)
            if(validate):
                print("\n/*/*/*/*Login Successfull*/*/*/*/")
                print(f":) :) welcome {username} :) :)\n")
                Patient.welcome(Password)
            else:
                print(" :( Enter Correct Values :(")
                Login.login_(1)
        if(profile==2):
            validate=access.verify(username,Password,profile)
            if(validate):
                print("\n/*/*/*/*Login Successfull*/*/*/*/")
                print(f"\n:) :) welcome {username} :) :)\n")
                Doctor.welcome(Password)
            else:
                print(" :| Enter Correct Values :|")
                Login.login_(2)

    def signup():
        print("\n:) :)Welcome To Sign Up page for Patient :) :)")
        first_name=input("Enter your First Name: ").lower()
        last_name=input("Enter your last name: ").lower()
        initial=input("Enter your initial: ").lower()
        loop=1
        while loop:
            phone_number=int(input("Enter your phone number: "))
            if phone_number>6000000000 and 9999999999>phone_number:
                username=input("Enter your username: ").lower()
                loop=1
                while loop:
                    password=input("Enter your password: ")
                    if re.search(passcheck,password) and len(password)>=8:
                        passw=password
                        loop=0
                    else:
                        print("\nUse Caps(1), small(1), number(1), Special Char(1), Must be in 8 Char")
                        print("!! Enter Strong password !!\n")
                        loop=1
                loop=0
            else:
                print("!! Give Valid Phone number !!")
                loop=1

        mydb = mysql.connector.connect(host = "localhost", user = "root",password = "Jay4prasanth@",database = "hms")
        cur = mydb.cursor()
        
        val=(first_name,last_name,initial,str(phone_number),str(username),str(passw))
        sql = "insert into Patient(first_name, last_name, initial, phone_number, username, password) values (%s, %s, %s, %s, %s,%s)"
        try:
            cur.execute(sql,val)
            mydb.commit()
        except:
            mydb.rollback()
        print("Data updated!")  
        mydb.close()  

        print("\n:) Login :)\n")
        Login.login_(1)