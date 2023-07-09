import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="coe")
mycursor = mydb.cursor()

from LogIn import LogIn
import re
import csv

class SignUp:
    def signUpPage():
        print("***SignUp Page***")
        while 1:
            #verify username
            uName=0
            uEmail=0
            uPass=0
            #verify=0
            userName=input("Enter your username:")

            query="select username from user where username=%s"
            mycursor.execute(query,(userName,))
            result=mycursor.fetchone()
            if result is not None:
                print("***This Username is already exist try with other username***")
                continue
            else:
                uName=1
            
            #verify email
            email=input("Enter your Email address:")
            pattern = r"^[a-z0-9_.+-]+@gmail\.com$"
            if re.match(pattern, email):
                query = "select email from user where email=%s"
                mycursor.execute(query,(email,))
                result = mycursor.fetchone()
                if result is not None:
                    print("***This Email is already exist try with other username***")
                    continue
                else:
                    uEmail=1
            else:
                print("***Email address is not valid***")
                continue

            #verify password
            password=input("Enter your password:")
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
            match = re.compile(reg)
            if re.search(match,password):
                uPass=1
                break
            else:
                print("***Password is not valid***")
                continue

        if uName ==1 and uEmail == 1 and uPass == 1:
            query="insert into user (username,email,password) values(%s,%s,%s)"
            values=(userName,email,password)
            mycursor.execute(query,values)
            mydb.commit()
            mycursor.close()
            mydb.close()
            print("***SignUp Successfully***")
            LogIn.LogInPage()

