import csv
from datetime import datetime,date
from Billing import Billing

roomSts=["1","no","2","yes","3","yes","4","yes","5","no","6","no","7","yes","8","no","9","yes","10","yes"]
nonDays=0
acDays=0
nonAllocate=[]
acAllocate=[]

class Room:
    def roomAvail():
        print("***Booking Page***")
        Rtype=int(input("Select the type of room you want\n1.Non-AC \n2.AC\n"))
        if Rtype==1:
            nonAc.nonAcMeth()
        elif Rtype==2:
            Ac.AcMeth()
        else:
            print("***Enter valid type***")
    #To book non-AC room

class nonAc:
    def nonAcMeth():
        print("Price per day: Rs.2000")
        nonAvail=0
        nonAllocate=[]
        for row in roomSts[:10]:
            if row=="yes":
                nonAvail+=1

        if not nonAvail==0:
            print("Available rooms:",nonAvail)
        else:
            print("***Rooms are currently UnAvailable***")
        while 1:
            #number of rooms required
            nonReq=int(input("Type how many rooms you want(in numbers):"))
            temp=nonReq
            if nonReq>nonAvail or nonReq<=0:
                print("***Enter vaild number***")
                continue
            #checkIn date
            checkIn=input("Check in date(dd-mm-yy):")
            if not vailidation.dateVerify(checkIn):
                continue
            else:
                Sdt=datetime.strptime(checkIn,"%d-%m-%Y")
                x=str(date.today().strftime("%d-%m-%Y"))
                tdy=datetime.strptime(x,"%d-%m-%Y")
                if Sdt >= tdy:
                    pass
                else:
                    print("***Enter vaild date***")
                    continue
            #checkOut date
            checkOut=input("Check out date(dd-mm-yy):")
            if not vailidation.dateVerify(checkOut):
                continue
            else:
                Edt=datetime.strptime(checkOut,"%d-%m-%Y")
                if Edt >= Sdt:
                    book=int(input("***Enetr the choice***\n1.Confirm your booking\n2.Cancel your booking\n"))
                    if book==1:
                        nonDays=(Edt-Sdt).days
                        print(nonDays)
                        for x in roomSts[:10]:
                            if x=="yes" and temp>0:
                                ind=roomSts.index(x)
                                roomSts[ind]="no"
                                nonAllocate.append(roomSts[ind-1])
                                temp-=1
                        nonAvail-=nonReq
                        print(nonAllocate)
                        alter=int(input("Do you want AC room?\n1.Yes\n2.No\n"))
                        if alter==1:
                            Ac.AcMeth()
                        elif alter==2:
                            Billing.Bill(nonDays,nonAllocate,acDays,acAllocate)
                            break
                        else:
                            print("***Enter vaild choice***")
                    elif book==2:
                        Room.roomAvail()
                    else:
                        print("***Enter vaild choice***")
                else:
                    print("***Enter vaild date***")
                    continue

    #To book AC room
class Ac:
    def AcMeth():
        print("Price: 3000 per day")
        acAvail=0
        acAllocate=[]
        print(nonDays)
        print(nonAllocate)
        for row in roomSts[10:20]:
            if row=="yes":
                acAvail+=1

        if not acAvail==0:
            print("Available rooms:",acAvail)
        else:
            print("***Rooms are currently UnAvailable***")

        while 1:
            #number of rooms required
            acReq=int(input("Type how many rooms you want(in numbers):"))
            temp=acReq
            if acReq>acAvail or acReq<=0:
                print("***Enter vaild number***")
                continue
            #checkIn date
            acCheckIn=input("Check in date(dd-mm-yy):")
            if not vailidation.dateVerify(acCheckIn):
                continue
            else:
                acSdt=datetime.strptime(acCheckIn,"%d-%m-%Y")
                acx=str(date.today().strftime("%d-%m-%Y"))
                actdy=datetime.strptime(acx,"%d-%m-%Y")
                if acSdt >=actdy:
                    pass
                else:
                    print("***Enter vaild date***")
                    continue
            #checkOut date
            acCheckOut=input("Check out date(dd-mm-yy):")
            if not vailidation.dateVerify(acCheckOut):
                continue
            else:
                acEdt=datetime.strptime(acCheckOut,"%d-%m-%Y")
                if acEdt >= acSdt:
                    acbook=int(input("***Enetr the choice***\n1.Confirm your booking\n2.Cancel your booking\n"))
                    if acbook==1:
                        acDays=(acEdt-acSdt).days
                        for x in roomSts[10:20]:
                            if x=="yes" and temp>0:
                                ind=roomSts.index(x)
                                roomSts[ind]="no"
                                acAllocate.append(roomSts[ind-1])
                                temp-=1
                        acAlter=int(input("Do you want Non-AC room?\n1.Yes\n2.No\n"))
                        if acAlter==1:
                            nonAc.nonAcMeth()
                        elif acAlter==2:
                            Billing.Bill(nonDays,nonAllocate,acDays,acAllocate)
                            break
                        else:
                            print("***Enter valid choice***")
                    elif acbook==2:
                        Room.roomAvail()
                    else:
                        print("***Enter vaild choice***")
                else:
                    print("***Enter vaild date***")
                    continue

    #date format validation
class vailidation:
    def dateVerify(check):
        format="%d-%m-%Y"
        try:
            return bool(datetime.strptime(check,format))
        except ValueError:
            print("***Enter the date in correct format")
            return False
        