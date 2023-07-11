import time
from getpass import getpass
class payment:
    def bill(seats):
        amount=(seats*100)
        entertainmenttax =25
        sgst=25
        print("Total Amount to pay(taxes included):",amount+entertainmenttax+sgst)
        print("PAYMENTS AVAILABLE:01.CARD PAYMENT 02.UPI")
        payment_type=int(input("CHOOSE THE MODE OF PAYMENT (1 OR 2):"))
        if payment_type==1:
          card_number=input("ENTER THE CARD NUMBER\n")
          account_name=input("ENTER THE ACCCOUNT HOLDER'S NAME\n")
          cvv=getpass(prompt="ENTER YOUR CVV")
        elif(payment_type==2):
          print("SCAN YOUR QR CODE FROM ANY OF YOUR UPI APPS")
          time.sleep(3)
        else:
          print("SELECT FROM THE GIVEN CHOICES")
        
