from seatAvailablitty import seatavailablity

class ticketavailablity:
    def info():
        movies=["VINAITHANDI VARUVAYA","VETTAIYADU VILLAIYADU","KAAKHA KAAKHA","NITHANEY EN PON VASANTHAM","VARANAM AYIRAM"]
        print("MOVIES ON-SCREEN:\n 0.VINAITHANDI VARUVAYA\n 01.VETTAIYADU VILLAIYADU\n 02.KAAKHA KAAKHA\n 03. NITHANEY EN PON VASANTHAM\n 04.VARANAM AYIRAM")
        movieavailable=int(input("ENTER THE CHOICES FROM 0-4\n"))
        if (movieavailable==0):
            print(movies[movieavailable])
            seatavailablity.info(movieavailable)
        elif (movieavailable==1):
            print(movies[movieavailable])
            seatavailablity.info(movieavailable)
        elif (movieavailable==2):
            print(movies[movieavailable])
            seatavailablity.info(movieavailable)
        elif (movieavailable==3):
            print(movies[movieavailable])
            seatavailablity.info(movieavailable)
        elif (movieavailable==4):
            print(movies[movieavailable])
            seatavailablity.info(movieavailable)
        else:
            print("CHOOSE THE CURRENT RUNNING MOVIE")






        