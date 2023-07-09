
class Billing:
    def head():
        print("~"*75)
        print("\t\t\tHOTEL TAJ")
        print("~"*75)
      
    def Bill(nonDays,nonAllocate,acDays,acAllocate):
        print(nonDays,nonAllocate,acDays,acAllocate)
        if (not nonDays==0) and (not acDays==0):
            Billing.head()
            print("Room.No\t\tType\t\tNo.of Days\t\tprice")
            totalPrice=0
            for x in nonAllocate:
                totalPrice+=(2000*nonDays)
                print(x,"\t\tNon AC\t\t",nonDays,"\t\t\t",nonDays*2000)
            for x in acAllocate:
                totalPrice+=(3000*acDays)
                print(x,"\t\tAC\t\t",acDays,"\t\t\t",acDays*3000)
            print("\t\t\t\t\t\tTotal:  ",totalPrice)
        elif (not acDays==0) and nonDays==0:
            Billing.head()
            print("Room.No\t\tType\t\tNo.of Days\t\tprice")
            totalPrice=0
            for x in acAllocate:
                totalPrice+=(3000*acDays)
                print(x,"\t\tAC\t\t",acDays,"\t\t\t",acDays*3000)
            print("\t\t\t\t\t\tTotal:  ",totalPrice)
        elif (not nonDays==0) and acDays==0:
            Billing.head()
            print("Room.No\t\tType\t\tNo.of Days\t\tprice")
            totalPrice=0
            for x in nonAllocate:
                totalPrice+=(2000*nonDays)
                print(x,"\t\tNon AC\t\t",nonDays,"\t\t\t",nonDays*2000)
            print("\t\t\t\t\t\tTotal:  ",totalPrice)
