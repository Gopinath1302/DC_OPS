from Product import item
import re
import mysql.connector
mydb = mysql.connector.connect(host="localhost" ,user="root",password="Selva@123",database="db1")
mycursor = mydb.cursor()

username="selva"
password="Selva@12"
class validate:
    def pass_valid(self,word):
            if (re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$",word)):
                return word
            else:
                print("Does not contain word or number or less than 6 letters \n Enter password again")
                word=input()
            
class login():
    def __init__(self,username,password):
            print("1.Login\n2.Register")
            temp=int(input("Enter 1 to  login or 2 to register: "))
            if temp == 1:
                login.authentication(self,username,password)
            if temp == 2:
                while 1:
                    username=input("Uname: ")
                    p=input("Password: ")
                    password=validate.pass_valid(self,p)
                    query="select username from user where username=%s"
                    mycursor.execute(query,(username,))
                    result=mycursor.fetchone()
                    if result is not None:
                        print("This is Username is already exists")
                        continue
                    else:
                        query="insert into user (username,password) values(%s,%s)"
                        values=(username,password)
                        mycursor.execute(query,values)
                        print("Registerd Successfull!!!\nLogin Please")
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                        login.authentication(self,username,password)
                        
                        
    def authentication(self,username,password):
        user=input("name: ") 
        pswd=input("password: ")
        check=validate.pass_valid(self,pswd)
        if login.verify_login(user,pswd):
            print("Login Success!\n\t\t\tWelcome to Zomato\t\t\t")
            print("Breakfast -> 1\nDinner -> 2")
            number = int(input())
            if(number == 1):
               item.breakfast(self)
            else:
               item.dinner(self)
        else:
            print(password)
            print("Enter Your Valid input:")
            login.authentication(self,username,password)  

    def verify_login(username, password):
        conn = mysql.connector.connect(host="localhost" ,user="root",password="Selva@123",database="db1")
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM user WHERE username=%s AND password=%s', (username, password))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result[0] > 0:
            return True
        else:
            return False 

Obj=login(username,password)
Obj.login
item()


