import time
class Payment():
    def payment(Total_Cost):
        print("")
        print("Make Your Payment Using:")
        print("1.Cash on Delivery.\n2.NetBanking.")
        print("*-----*-----*-----*-----*-----*")
        print("")
        Pay=int(input("Use Payment Method as : "))
        if Pay==1:
            print("Your Total Cost: Rs.",Total_Cost)
            print("!... Your Order Has Been Placed for Delivery...!")
            time.sleep(2)
            print("Pay It While Delivering")
            print("Healthy Shopping...")
            print("*-----*-----*-----*-----*-----*")
            print("")


        elif Pay==2:
            print("Your Total Cost: Rs.",Total_Cost)
            print("Redirecting to Google Pay...")
            time.sleep(2)
            print("Your Payment is Sucessfull...")
            time.sleep(3)
            print("!...Your Order Has Been Placed for Delivery...!")
            print("*-----*-----*-----*-----*-----*")
            print("")
                    
        else:
            print("You have selected Invalid Payment method...")
        