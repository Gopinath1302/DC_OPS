import re
import Database_Connection
from Database_Connection import connection,global_cursor
from view_items import Viewitems

class New_Registration:
    user_name : str = ''
    user_password : str = ''
    user_phonenumber : int = 0
    user_emailId : str = ''
    @classmethod
    def new_user(self):
        print("_"*100)
        print("-"*40,"Sign-Up Module","-"*40)
        print("_"*100)
        flag = True
        while flag:
            user_name = input("Enter your Name\n")
            regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
            constraint = re.compile(regex)
            if (re.search(constraint,user_name)):
                flag = False
            else:
                print("you have entered a Invalid user name please try with valid one:)")
        

        flag = True
        while flag:
            user_password = input("Enter your Password\n")
            regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"
            constraint = re.compile(regex)
            if (re.search(constraint,user_password)):
                flag = False
            else:
                print("you have entered a Invalid password please try with valid one:)")


        flag = True
        while flag:
            try:
                user_phonenumber = int(input("Enter your Mobile number\n"))
            except:
                print("you have entered a Invalid mobile number please try with valid one:)")
            else:
                if user_phonenumber > 6000000000 and user_phonenumber < 10000000000 and user_phonenumber != 6666666666 and user_phonenumber != 7777777777 and user_phonenumber != 8888888888 and user_phonenumber != 9999999999:                    
                    flag = False
        flag= True
        while flag:
             user_emailId = input("Enter your Email address:")
             regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
             match = re.compile(regex)
             if (re.search(match, user_emailId)):             
                flag = False
             else:
              print("Please, Enter your Valid Email Address:")
        query = "insert into user_details values(%s,%s,%s,%s);"
        global_cursor.execute(query, (user_name,user_password, str(user_phonenumber),user_emailId))
        connection.commit()
        print("\n", "-" * 25, ">Successfully registered as the User<", "-" * 25)
                
    
class Login(New_Registration):
       
    __user_name = ""
    __password  = ""
    @classmethod
    def login(self):
        print("\n")
        print("-"*100)
        print("*"*40,"Login Module","*"*40)
        print("-"*100)
        print("\n")
        flag1 = True
        while flag1:
            __user_name = input("Enter your Name:      ")
            __password = input("Enter your Password:  ")
            query = "Select * from user_details where user_name=%s;"
            global_cursor.execute(query,(__user_name,))
            result = global_cursor.fetchone()
            try:
                if __password == result[1]:
                    print("\n")
                    print("-"*100) 
                    print(" "*10+"*"*20+"Hi you are loggen in successfully"+"*"*20+" "*10)
                    print("-"*100)
                    print("\n")        
                    flag = True
                    while flag:
                        try:                           
                            print("1 for view items")
                            print("2 for view profile")
                            print("Press any number key to goto login page")
                            choice = int(input("Enter your choice\t"))
                        except:
                            print("you have entered a Invalid key:)")
                        else:
                            if choice == 1:
                                Viewitems().viewitems()
                            elif choice == 2:
                                print("Name       :     "+result[0])
                                print("Password   :     "+result[1])
                                print("phone N.O. :     "+result[2])
                                print("E-mail     :     "+result[3])
                                print("\n")
                                flag = True
                            else:
                                flag = False
                else:
                    print("you have entered a wrong user name / password")
            except TypeError:
                print("Invalid entry")
            print("\t\t\t1.for continue login\t\t\t\t\t2.for return to home screen")
            choice = int(input("Enter your choice\t"))
            if choice == 1:
                flag1 = True
            elif choice == 2:
                flag1 = False
            else:
                print("Invalid entry")
        
       
