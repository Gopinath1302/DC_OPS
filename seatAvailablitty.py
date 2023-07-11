from payment import payment

class seatavailablity:
    def info(movieavailablity):
        if(movieavailablity==0):
            print("Total no seats available for this show: 100")
        if(movieavailablity==1):
            print("Total no seats available for this show: 80")
        if(movieavailablity==2):
            print("Total no seats available for this show: 50")
        if(movieavailablity==3):
            print("Total no seats available for this show: 30")
        if(movieavailablity==4):
            print("Total no seats available for this show: 100")
        seats=int(input("Enter the no of seats you need:"))
        payment.bill(seats)
        print("PAYMENT SUCCESSFULL")
        


