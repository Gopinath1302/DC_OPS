class Payment:
    def payment(self,bill):
        pay=int(input("Choose the Payment method \n1.Cash On Delivery\n2.UPI payment :"))
        if(pay==1):
            print("                 Your Total amount is:",bill)
            print("............Pay it while delivering........")
        elif(pay==2):
            print("                 Your Total amount is:",bill)
            print("                 Payment Successful")
            print("                 Visit Again")
            