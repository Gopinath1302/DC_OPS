from authenticate import auth
from authenticate import Register


class Choice:
    @staticmethod
    def first():
        print("Welcome to RG Book Store")
        print("--------------------------------------------------")
        flag = True
        while flag:
            print("Enter 1 for Register")
            print("Enter 2 for Login")
            print("Enter 3 for Logout")
            try:
                op = int(input())
            except ValueError:
                print("Enter Only Numbers")
            else:
                flag = False
                if op == 1:
                    Register.getin()
                elif op == 2:
                    new = auth()
                    new.login()
                elif op == 3:
                    print("logout")
                else:
                    flag = True
                    print("Enter option Correctly")
