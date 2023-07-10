import re
import mysql.connector
from authentication import access
passcheck= r'^[a-z to A-Z to 0-9]+[!@#$%^&*()_+]?\w{0,5}$'
class call:
    def ad():
        username=input("Enter your username: ").lower()
        password=input("Enter your Password: ")
        try:
            prof=3
            access1=access.verify(username,password,prof)
            val=True
            call.admin_fun(access1,val)
        except IndexError:
            print("\n???Enter Correct Values???\n")
    def admin_fun(access1,val):
        while val:
            if access1:
                value=int(input("""\nWant to Perform: \nAdd Doctor(1) or delete Doctor(2) or Add Admin(3) or View Doctor Details(4) or 
View Patient Details(5) or Logout(6)  """))
                if value==1:
                    print("\nSignup for Doctor")
                    first_name=input("\nEnter Doctor First Name: ").lower()
                    last_name=input("Enter last name: ").lower()
                    initial=input("Enter initial: ").lower()
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
                            print("\n!! Give Valid Phone number !!\n")
                            loop=1
                    specialist=input("Enter the speciality of Doctor: ").lower()
                    available=input("Enter availability yes or no: ").lower()

                    mydb = mysql.connector.connect(host = "localhost",
                                                   user = "root",
                                                   password = "Jay4prasanth@",
                                                   database = "hms")
                    cur = mydb.cursor()
                    
                    val=(first_name,last_name,initial,str(phone_number),str(username),str(password),specialist,available)
                    sql = "insert into Doctor(first_name, last_name, initial, phone_number, username, password, specialist, available) values (%s, %s, %s, %s, %s,%s,%s,%s)"
                    try:
                        cur.execute(sql,val)
                        mydb.commit()
                    except:
                        mydb.rollback()
                    print("Data updated!")  
                    mydb.close()

                    call.admin_fun(1,True)
                elif value==2:
                    username=input("\nEnter Doctor username: ").lower()
                    password=input("Enter password to Delete: ")
                    passw=password
                    prof=2
                    access1=access.verify(username,password,prof)
                    if access1:
                        mydb = mysql.connector.connect(host = "localhost",
                                                    user = "root",
                                                    password = "Jay4prasanth@",
                                                    database = "hms")
                        cur = mydb.cursor()
                        try:
                            cur.execute(f"delete from Doctor where password = {passw}")
                            mydb.commit()
                        except:
                            mydb.rollback()
                        mydb.close()  
                        call.admin_fun(1,True)
                    else:
                        print("Given data is not in List")
                        call.admin_fun(1,True)
                elif value==3:
                    print("\n       <<<<<<<<<<<|| You have rights BUT... Sorry ||>>>>>>>>>>>>       ")
                    call.admin_fun(1,True)
                elif value==4:
                    mydb = mysql.connector.connect(host = "localhost",
                                                   user = "root",
                                                   password = "Jay4prasanth@",
                                                   database = "hms")
                    cur = mydb.cursor()
                    try:
                        cur.execute("select * from doctor order by first_name")
                        result = cur.fetchall()
                        print("\nfirst_name    last_name    initial    phone_number    username    password    specialist    available\n")
                        for loop in result:
                            print("%s      %s       %s     %s      %s      %s      %s      %s"%(loop[0],loop[1],loop[2],loop[3],loop[4],loop[5],loop[6],loop[7]))
                    except:
                        mydb.rollback()
                    mydb.close()
                    call.admin_fun(1,True)
                elif value==5:
                    mydb = mysql.connector.connect(host = "localhost",
                                                   user = "root",
                                                   password = "Jay4prasanth@",
                                                   database = "hms")
                    cur = mydb.cursor()
                    try:
                        cur.execute("select * from patient order by first_name")
                        result = cur.fetchall()
                        print("\nfirst_name     last_name     initial     phone_number    username    password\n")
                        for loop in result:
                            print("%s     %s      %s     %s     %s      %s"%(loop[0],loop[1],loop[2],loop[3],loop[4],loop[5]))
                    except:
                        mydb.rollback()
                    mydb.close()
                    call.admin_fun(1,True)
                elif value==6:
                    print("\n :) :) Come Another Time :) :)")
                    exit()
                else:
                    print("\n???Enter valid Option???")
            
            else:
                print("Either Username or Password Wrong\n")
                print("~~Back to Login~\n")
                call.ad()