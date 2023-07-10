import re
import mysql.connector
passcheck= r'^[a-z to A-Z to 0-9]+[!@#$%^&*()_+]?\w{0,5}$'
class Patient:
    def welcome(password1):
        while True:
            option=int(input(("""\nList of doctors(1) or Change PhoneNumber(2) or 
Change Password(3) or Logout(4)  """)))
            if option==1:
                myconn =mysql.connector.connect(host = "localhost",
                                                user = "root",
                                                password = "Jay4prasanth@",
                                                database = "hms")
                cur = myconn.cursor()
                try:
                    cur.execute("select first_name,phone_number,specialist,available from Doctor order by first_name")
                    result = cur.fetchall()
                    print("\nName      Phone number      Specialist      Availability")
                    for row in result:
                        print("%s      %s      %s      %s"%(row[0],row[1],row[2],row[3]))
                except:
                    myconn.rollback()
                myconn.close()
            elif option==2:
                myconn =mysql.connector.connect(host = "localhost",
                                        user = "root",
                                        password = "Jay4prasanth@",
                                        database = "hms")
                cur = myconn.cursor()
                try:
                    password2=(password1)
                    choice=int(input("\nWant to change phone number(1) or Not(2) "))
                    if choice==1:
                        loop=1
                        while loop:
                            ph=int(input("Enter New number: "))
                            if ph>6000000000 and 9999999999>ph:
                                ph=(ph)
                                cur.execute("update patient set phone_number = %s where password=%s",(ph,password2))
                                loop=0
                            else:
                                print("\n!! Give Valid Phone number !!\n")
                                loop=1
                        print("\nUpdated!\n")
                        myconn.commit()
                    elif choice ==2:
                        print("Great ")
                        Patient.welcome(password2)
                    else:
                        print("\nInvalid Option")
                except:
                    myconn.rollback()
                myconn.close()
                print("\n")
            elif option==3:
                myconn =mysql.connector.connect(host = "localhost",
                                        user = "root",
                                        password = "Jay4prasanth@",
                                        database = "hms")
                cur = myconn.cursor()
                try:
                    choice=int(input("\nWant to change password(1) or Not(2) "))
                    if choice==1:
                        loop=1
                        while loop:
                            pho=[]
                            cur.execute("select phone_number from patient")
                            result = cur.fetchall()
                            for row in result:
                                pho.append(row[0])
                            username_flag=False
                            phon=int(input("Enter Phone number to change password: "))
                            phon=str(phon)
                            for i in pho:
                                if phon==i:
                                    username_flag=True
                            if username_flag:
                                loop=1
                                while loop:
                                    passw=input("Enter New password: ")
                                    if re.search(passcheck,passw) and len(passw)>=8:
                                        passw=str(passw)
                                        cur.execute("update patient set password =%s where phone_number=%s ",(passw,phon))
                                        loop=0
                                    else:
                                        print("\nUse Caps(1), small(1), number(1), Special Char(1), Must be in 8 Char")
                                        print("!! Enter Strong password !!\n")
                                loop=0
                            else:
                                print("Enter Correct Phone number to change password")
                        print("\nUpdated!\n")
                        myconn.commit()
                    elif choice ==2:
                        pass
                    else:
                        print("\nInvalid Option")
                    
                except:
                    myconn.rollback()
                myconn.close()
                print("\n")
            elif option==4:
                print("\n:) Take Care of Your Health... :)")
                break
            else:
                print("\n:( Enter Valid Option :(")