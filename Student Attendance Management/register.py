import re
from Addstudent import student
from manage import manage_attendance
from close import Logout
from dbconnection import conn,cur
class Register():
    @classmethod
    def signup(self):
        print("\n*----------Signup----------*\n")
        Username = input("Enter Username : ")
        Email = input("Enter Email : ")
        if re.match(r"^(?=.*[a-z])(?=.*[0-9])(?=.*[@.])",Email):
            print("     Valid Email        ")
            password=input("Enter password: ")
            if re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[*@#$!%^&{}])(?=.*[0-9])",password):
                print("     Strong password    ")
                Reenter_password=input("Reenter Password : ")
                if(Reenter_password == password):
                    data=(Username, Email, password)
                    query="insert into staffdetails values(%s, %s, %s)"
                    cur.execute(query,data)
                    conn.commit()
                    print("\n*------Registration is successful------*")
                    Register.login(self)
                else:
                    print("Not matched")
            else:
                print("Weak password")
        else:
            print("Invalid Email")
    
    def login(self):
        print("\n*----------Login----------*\n")
        User_name = input("Enter Username : ")
        E_mail = input("Enter Email : ")
        pass_word = input("Enter Password : ")
        Query="select * from Staffdetails where (Emaillist=%s and Passwordlist=%s)"
        Data=(E_mail,pass_word)
        cur.execute(Query, Data)
        a=cur.fetchone()
        if a:
            print("\n*-------Login Successful-------*")
            print("\n\t\t\t\tWelcome to Staff Dashboard\t\t\t\t")
            print("1 - Add student\n2 - View students details\n3 - Manage attendance\n4 - Logout")
            try:
                number=int(input("\nEnter choice : "))
                if(number==1):
                    student.addstudent(self)
                elif(number==2):
                    student.viewdetails(self)
                elif(number==3):
                    manage_attendance.manage(self)
                elif(number==4):
                    Logout.logout(self)
                else:
                    print("Enter valid number")
            except ValueError:
                print("Enter an integer")
        else:
            print(" Invalid Username or password")
        