from c_account import c_Account 
from c_account import logincls
class optioN():
    @classmethod
    def user (self):
        flag = True
        while flag:
            print("\n1. Register")
            print("2. Login")
            print("3. Logout")
            try:
                value=int(input("\tEnter your chioce:\t"))
            except:
                print("\t\t\t\t\tInvalid entry!\nPlease entry a valid choice")
            if value==1:
                c_Account.Register()
            elif value==2:
                logincls().Login()
            elif value==3:
                print("_"*50,"Logout successfully","_"*50)
                quit()
            
