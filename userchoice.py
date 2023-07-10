from validation import New_Registration
from validation import Login
class Userchoice():
    @classmethod
    def userChoice(self):
        print("-"*100)
        print(" "*30 +"Welcome Online Grocery store")
        print("-"*100)
        flag = True
        while flag:    
            print("Enter 1 for New Registration")
            print("Enter 2 for Login")
            
            choice = int(input("Enter Your Choice:\t"))
            if choice == 1:
                New_Registration.new_user()
            
            elif choice == 2:
                Login.login()
             
            else:
                print("There is no Such Kind of action")
            

