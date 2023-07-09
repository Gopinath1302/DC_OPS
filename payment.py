import time
class pay():
    @classmethod
    def payment(self):
        print("--------------------------------------------------")
        print("Enter 1 for Gpay")
        print("Enter 2 for Net Banking")
        print("Enter 3 for Cash on delivery")
        flag=True
        while flag:
         try:  
          pay_op=int(input())
         except ValueError:
           print("Enter only numbers")
         else:
          if pay_op==1:
            print("Enter Your UPI id")
            id=input()
            print("Please wait Redirecting to Gpay")
          elif pay_op==2:
            print("Enter Your Netbanking Id")
            id=input()
            print("Please wait Redirecting to Your Bank")
          elif pay_op==3:
            print("Pay when order is delivered") 
          elif pay_op>3:
            flag=True
            print("Enter only given option")
            continue
          time.sleep(2)
          print("\nOrder Placed") 
          print("Thank You Visit Again")