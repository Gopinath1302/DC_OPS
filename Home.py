from SignUp import SignUp
from LogIn import LogIn

class Home:
    def homePage():
        while 1:
            choice = input("Enter the choices: \n1.Sign Up \n2.Login \n3.Exit\n")
            if choice == '1':
                SignUp.signUpPage()
                break
            elif choice == '2':
                LogIn.LogInPage()
                break
            elif choice == '3':
                print("Exit")
                break
            else:
                print("Enter valid choice")
                continue

