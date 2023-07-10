from MakePayment import Payment
class OrderMed:
    def ordermed(cost,index):
        Medstock = [20,20,20,20,20]
        quantity=int(input("Enter Quantity:"))
        if(quantity<=Medstock[index]):
            Tcost=(cost * quantity)
            print("Total Cost:",Tcost)
            print("*-----*-----*-----*-----*-----*")
            print("")
            print("1.MakePayment.\n2.Cancel Order.")
            Verify=int(input("Enter Your Choice:"))
            if Verify==1:
                Payment.payment(Tcost)
            elif Verify==2:
                print("Your Order Has Been Cancelled....")
                print("*-----*-----*-----*-----*-----*")
                print("")
        else:
            print("Selected Medicine is Out Of Stock...")
            print("*-----*-----*-----*-----*-----*")
        