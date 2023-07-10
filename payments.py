import time
class Payments:
    def paymentchoice(self):
        print("1 for Net Banking")
        print("2 for Credit / Debit card")
        print("3 for Cash on delivery")
        print("4 for UPI Payment")
        paymentchoice = int(input("Enter your choice:\n"))
        if paymentchoice == 1:
           
           bank_name = input("Type your Bank name")
           time.sleep(5)
           print("Please wait we are redircting your bank server")
           pin = int(input("Enter your Transaction pin"))
           if pin == 1234:
               time.sleep(10)
               print("Thank you For your purchase, visit agin")
           else:
               print("You have entered An incorrect pin")

        elif paymentchoice == 2:
           card_number = int(input("Enter your card number"))
           if card_number >1000000000000000 and card_number < 9999999999999999:
               time.sleep(5)
               pin = int(input("Enter your pin"))
               if pin == 1234:
                  time.sleep(10)
                  print("Thank you For your purchase, visit agin")
               else:
                   print("You have entered An incorrect pin")
        elif paymentchoice  == 3:
           print("Your Oreder willbe Arriving Soon")
           print("Thank you For your purchase, visit agin")
        elif paymentchoice  == 4:
           upi_id = input("enter your upi-id")
           pin = int(input("Enter your transaction pin"))
           if pin == 1234:
              print("Please wait we are redircting your bank server")
              time.sleep(5)
              print("Thank you For your purchase, visit agin")
           else:
               print("You have entered An incorrect pin/upi_id")
        else:
            print("Please select valid payment method")
