from ViewMedPro import MedProducts
from dbconnection import connection,my_cursor
import time
import re
import getpass
Echeck=r'^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]+\w+[.]\w{2,3}$'
Pcheck=r'^[A-Z]?[a-z0-9]+[!@#$%^&*()_+]?\w{0,3}$'
# UEmail=" "
# Upassword=" "
# Uphonenumber=""
# Uusername=" "

class Signup():  
    @classmethod
    def signupch(self):
        v=True
        while v:
            User_Name= input("Enter UserName:  ")
            #Uusername.append(User_name)
            Email =input("Enter Email Id:  ")
            print("Enter Password that should :\n1.Starts with Capital Letter\n2.If you need Use Special Character(1)\n3.Note after Special Character 0 or 3 alphanumeric is accepted")
            Password = input("Enter Password:  ")
            if (re.search(Echeck,Email)):
                #UEmail.append(Email)
                if (re.search(Pcheck,Password)):
                    #Upassword.append(Password)
                    print("@Strong Password@")
                    v=False
                else:
                    print("\t\t\t<<<<<<<Not Valid a password>>>>>>>\t\t\t")
            else:
                print("\t\t\t<<<<<<<Not Valid Email Id>>>>>>>\t\t\t")
        flag = True
        while flag:
            try:
                PhoneNumber= int(input("Enter your Mobile number: "))
                if PhoneNumber > 6000000000 and PhoneNumber < 10000000000:
                    pass
                else:
                    print("\t\t\t<<<<<<<Enter the valid one>>>>>>>\t\t\t")

            except:
                print("\t\t\tYour Mobile Number entered is '<<<<Not Valid>>>>' try with a valid number\t\t\t")
            else:
                if PhoneNumber > 6000000000 and PhoneNumber < 10000000000:
                    #Uphonenumber.append(PhoneNumber)
                    #print("\t\t\t\t!*!*!*!*!...Your Registration is Successful...!*!*!*!*!\t\t\t\t")
                    flag = False
        credent="insert into user_details values(%s,%s,%s,%s);"
        my_cursor.execute(credent, (User_Name,Email,Password,PhoneNumber))
        connection.commit()
        time.sleep(2)
        print("\t\t",'!*'*10,"...Your Registration is Successful...",'!*'*10,"\t\t")

class Login():
    def __init__(self):
       self.UserName =" "
       self.UserPassword = " "

    @classmethod
    def signinch(self):
        flag=True
        while flag:
            self.UserName =input("Enter UserName:  ")
            self.UserPassword =getpass.getpass("Enter UserPassword:  ")
            print("*" *len(self.UserPassword)) 
            my_cursor.execute("SELECT * FROM user_details WHERE User_name = %s AND Password = %s",(self.UserName,self.UserPassword))
            #query = "Select * from user_details where user_name= ?,;"
            #my_cursor.execute(query,(self.UserName,))
            user = my_cursor.fetchone()
            if user is not None:
                print("\t\t\tHai",user[0],"you have Logged in Sucessfully:)\t\t\t")
                time.sleep(2)
                print("\t\t\t",user[0],"Welcome to Sasi Pharmacy:)\t\t\t")
                print("")
                print("View Medicine Products")
                MedProducts.medProducts()
                flag=False
                #return True
            else:
                print("\t\t\t<<<<<<<Invalid User>>>>>>\t\t\t")
                print("\t\t\t<<<<<<<Enter a Valid User Name and Password>>>>>>>\t\t\t")
                flag=False
            #return false
            
            # print("success")
            # flag=False
            #if result[0] == self.UserName:
            # if self.UserPassword ==  result[1]:
            #     print("\t\t\tHai",result[0],"you have Logged in Sucessfully:)\t\t\t")
            #     time.sleep(2)
            #     print("\t\t\t",result[0],"Welcome to Sasi Pharmacy:)\t\t\t")
            #     print("")
            #     print("View Medicine Products")
            #     MedProducts.medProducts()
            # else:
            #     print("\t\t\t<<<<<<<Invalid User>>>>>>\t\t\t")
            #     print("\t\t\t<<<<<<<Enter a Valid User Name and Password>>>>>>>\t\t\t")



            








