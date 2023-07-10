from Credentials import Signup
from Credentials import Login
class Choice_preference:
    @classmethod
    def choice(self):
        print("\t\t\t\t*.*.*.*.*.*Welcome To Sasi Pharmacy*.*.*.*.*.*\t\t\t\t")
        C=True
        while C:
            print("1.Signup / 2.Login/ 3.Logout")
            try:
                choices = int(input("Enter your choice: "))
            except:
                print("\t\t\tYou have entered invalid choice,enter numbers\t\t\t")
            else:
                if choices == 1:
                    Signup.signupch()
                elif choices == 2:
                    Login.signinch()   
                elif choices == 3:
                    print("\t\t\t.*.*.*.*.*.*.*.*.(THANK YOU FOR VISITING US!!!).*.*.*.*.*.*.*.*.\t\t\t")
                    C= False
                else:
                    print("\t\t\t<<<<<<<Invalid Choice>>>>>>>\t\t\t")