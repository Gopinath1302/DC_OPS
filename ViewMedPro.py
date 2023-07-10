from ViewMedCart import MedCart
from dbconnection import connection,my_cursor
from decimal import Decimal
MedNameList=[]
Price_List=[]
class MedProducts():
    @classmethod
    def medProducts(self):
        global flag
        flag = True
        while flag:
                print("")
                print("1.OTC Medicine")
                print("2.Skin Care")
                Pro_choice=int(input("Enter Product Choice: "))
                print("*-----*-----*-----*-----*-----*")
                ###OTC MEDCINE###
                if(Pro_choice == 1):
                    print("OTC MEDICINES")
                    print("-------------")
                    # Otcmed=["aspirin","Gaviscon","Cepacol","Cetirizine","Paracetamol"]
                    # OTC_Price=[11,86.5,63.5,17.5,12]
                    Med="select * from OTC_Med"
                    my_cursor.execute(Med)
                    result = my_cursor.fetchall()
                    for i in range(len(result)):
                        print(result[i][0]," : Rs.",result[i][1])
                    print("*-----*-----*-----*-----*-----*")
                    print("")
                    print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")    
                    Eo_choice = int(input("Enter Otc-Medicine no: "))
                    for i in range (len(result)):
                        if (i == (Eo_choice-1)):
                            print("Medicine: ",result[i][0]," - Rs",result[i][1])
                            my_cursor.execute("insert into view__med  values(%s,%s)",(result[i][0],result[i][1]))
                            connection.commit()
                            # # MedNameList.append(result[i])
                            # # Price_List.append(result[i])
                            print("Selected Medicine is added to the Cart")
                            print("*------*-----*-----*-----*-----*------*")
                            print("")
                            print("1.View Cart \n2.Add Medicine \n3.Skip")
                            k=int(input("Enter Your Choice: "))
                            if k==1:
                                 MedCart.view_medcart(result[i][0],result[i][1])
                                 flag = False
                            elif k==2:
                                 self.medProducts()
                            else:
                                 print("***Skipped Here***")
                                 print("*-----*-----*-----*-----*-----*")                               
                ###SKIN_CARE####
                elif (Pro_choice == 2):
                    print("SKIN CARE MEDICINES")
                    print("--------------------")
                    Med="select * from Sc_Med"
                    my_cursor.execute(Med)
                    result = my_cursor.fetchall()
                    # Skin_Care=["Calamine Lotion","cetaphil gentle","Eucerin Cream","Differin 0.1 gel","Isotretinoin"]
                    # Sc_Price=[125,184.5,167.6,263.5,778]
                    for i in range(len(result)):
                        print(result[i][0],": Rs. ", result[i][1])
                    print("*-----*-----*-----*-----*-----*")
                    print("")
                    print("If you want to select the medicine,enter the numbers (no alphabets & no special characters)")    
                    ES_choice = int(input("Enter Skin care - Medicine no: "))
                    for i in range (len(result)):
                            if (i == (ES_choice-1)):
                                print("Skin Care Product: ",result[i][0]," - Rs",result[i][1])
                                my_cursor.execute("insert into view__med  values(%s,%s)",(result[i][0],result[i][1]))
                                connection.commit()
                                # MedNameList.append(Skin_Care[i])
                                # Price_List.append(Sc_Price[i])
                                print("Selected Medicine is added to the Cart")
                                print("*------*-----*-----*-----*-----*------*")
                                print("")
                                print("1.View Cart \n2.Add Medicine \n3.Skip")
                                k=int(input("Enter Your Choice: "))
                                if(k==1):
                                    MedCart.view_medcart(result[i][0],result[i][1])
                                    flag = False
                                elif k==2:
                                    self.medProducts()
                                else:
                                    print("***Skipped Here***")
                                    print("*-----*-----*-----*-----*-----*")
                
                else:
                    print("You Have Selected a Invalid Choice...!!")


        

    

                        









