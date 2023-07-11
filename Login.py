from Validation import Validation
from Select import Display
from Server import db,cursor

class User:
    #user = {"Dharsana": "1234@06", "Devi": "123*"}
    

    def home(self):

        print("\n            >>>>>>>>>>>>>>>Welcome To Online Cosmetic Shoping>>>>>>>>>>>>>>>>>> ")
        print("""
            1 -> Register
            2 -> Login
            3 -> Exit
            """)
        flag=True
        while flag:  
            try:
                choice = int(input("Enter your Choice: \n"))
            except:
                print("-----------------You have choose the wrong Type----------------")
            else:
                flag=False
                if choice == 1:
                    User().register()
                elif choice == 2:
                    User().login()
                elif choice==3:
                    print("-------------------Thank you, You can visit here anytime!----------------------")
                elif choice>3:
                    print("Enter the given option")
                    flag=True    
   
    def register(self):
        username = input("Please enter your username: ")
        password = input("Please enter your Password: ")
        Validation().validate()
        # validation().validatePhone()
        #self.user.update({username: password})
        # print(self.user)
        query="insert into login (username,password) values(%s,%s)"
        values=(username,password)
        cursor.execute(query,values)
        db.commit()
        cursor.close()
        db.close()
        print("******************Account Created Successfully ********************")
        User().login()

    def login(self):
        name = input("Please enter your username: \n")
        password = input("Please enter your Password: \n")
        # Validation().validate()
        for key,value in self.user.items():
            if key==name and value==password :
                print("**********Login Successful**********")
                Display().select()
                break
            
        else:
            print("*********Username or Password is Incorrect***************")
            another_choice=int(input("1.Try again \n2.Register "))
            if another_choice==1:
                User().login()
            else:                            
                print("///////////////Register Your Account///////////////////")
                #User.register=classmethod(User.register)
                User().register()
           
    