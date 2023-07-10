class payment():
    def pay():
        while True:
            try:
                print("Enter the Payment Method\n1.Gpay\n2.Cash-On-Deivery")
                value = int(input())
                if(value == 1):
                    print("Enter Your upid ")
                    upi = input()
                    print("Your Order is Placed")
                    break
                elif(value == 2):
                    print("Pay at Desired Location")
                    break
            except Exception:
                print("Payment Failed!")

payment()