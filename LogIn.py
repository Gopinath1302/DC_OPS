import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="coe")
mycursor = mydb.cursor()

import csv
from Availability import Room

class LogIn:
    def LogInPage():
        print("***Login Page***")

        while 1:
            un=input("Enter your username:")
            pw=input("Enter your password:")
            query="select username,password from user where username=%s and password=%s"
            mycursor.execute(query,(un,pw,))
            res=mycursor.fetchone()
            if res:
                print("***Login successfully***")
                Room.roomAvail()
            else:
                print("***Incorrect Username or password***")
                continue

            mydb.commit()
            mycursor.close()
            mydb.close()
