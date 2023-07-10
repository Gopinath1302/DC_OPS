import re
import time
import db_connect
from db_connect import mydb, myobject 
from search import Search
class c_Account():
        cust_name : str = ''
        cust_password : str = ''
        cust_phonenumber : int = 0
        cust_emailId : str = ''
        @classmethod
        def Register(self):
            print("-"*50,"Sign","-"*50)
            flag = True
            while flag:
                cust_name=input("\n\tEnter your name:\t")
                regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
                constraint = re.compile(regex)
                if (re.search(constraint,cust_name)):
                    flag = False
                else:
                    print("you have entered a Invalid user name please try with valid one:)")
            flag = True
            while flag: 
                try:
                    cust_phonenumber = int(input("Enter your phone number:\t"))
                except:
                    print("\t\tInvalid phone number!\tPlease try  to enter a valid phone number")
                else:
                    if cust_phonenumber > 6000000000 and cust_phonenumber < 10000000000 and cust_phonenumber != 6666666666 and cust_phonenumber != 7777777777 and cust_phonenumber != 8888888888 and cust_phonenumber != 9999999999: 
                        flag = False
            flag=True
            while flag:
                cust_password=input("\tEnter the password:\t")
                regex = ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
                rule = re.compile(regex)
                if(re.search(rule,cust_password)):
                    flag =False
                else:
                    print("\t invaild password \t Try again")
            flag =True
            while flag:
                cust_emailId=input("\tEnter the EmailId:\t")
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                match = re.compile(regex)
                if (re.search(match, cust_emailId)):             
                    flag = False
                else:
                    print("Please, Enter your Valid Email Address")
            Query = "insert into cust_details values(%s,%s,%s,%s);"
            myobject.execute(Query,(cust_name, str(cust_phonenumber),cust_password,cust_emailId))
            mydb.commit()
            print("\n", "-" * 25, "Successfully registered as the User", "-" * 25)
            logincls().Login()
class logincls(c_Account):
        @classmethod
        def Login(self):
            print("_"*50,"Login","_"*50)
            cust_name=input("\n\tEnter your name:\t")
            cust_password=input("\tEnter your Password:\t")
            Query="select * from cust_details where (cust_name=%s and cust_password=%s)"
            myobject.execute(Query,(cust_name,cust_password,))
            sum= myobject.fetchone()
            try:
                if sum:
                    print("_"*50,"Login sucessfully","_"*50)    
                    print("_"*50,"view Details","_"*50)
                    print("\n1 . view profile")
                    print("2 . search place")
                    print("3 . Logout  ")    
                    try:
                        option=int(input("\tEnter your chioce:\t"))
                        if option==1:
                            print(sum[0])
                            print(sum[1])
                            print(sum[2])
                            print(sum[3])
                            time.sleep(5)
                            Search().place()
                        if option ==2:
                            Search().place()
                        elif option==3:
                            print("_"*50,"you have successfully Logout","_"*50)
                    except ValueError:
                        print("\t\tEnter an integer")
                else:
                    print(" \t\tInvalid Username or password")
            except:
                print("\t\tPlease try again")
                            


                


        



        
