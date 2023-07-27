from login import Login
from admin import call
class greeting:
    def message():
        while True:
            try:
                value=int(input("\nLogin(1) or Signup only for Patient(2) "))
                if value ==1:
                    print("\nLogin in Patient(1) or Doctor(2) or Admin(3)")
                    try:
                        val = int(input("Enter Your Option: "))
                        if val==1:
                            Login.login_(1)
                        elif val == 2:
                            Login.login_(2)
                        elif val==3:
                            print("\n*****WELCOME ADMIN*****")
                            call.ad()
                        else:
                            print("\n :( Invalid option:(")
                    except ValueError:
                        print("\n :( Incorrect value :(")
                        greeting.message()
                elif value == 2:
                    Login.signup()
                else:
                    print("\n :( Invalid option :( \n")
            except ValueError:
                print("\n :( Invalid Option :( \n")