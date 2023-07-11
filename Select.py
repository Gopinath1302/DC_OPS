from Payment import Payment

List=["\t1.Ornaments","\t2.Perfume","\t3.MakeupSet"]
    
class Display:
    bill = 0
    
    
    def select(self):
            print("The products available are:")
            length=len(List)
            for length in List:
                itr=0
            while itr < len(List):
                print(List[itr])
                itr+=1
            # print("initial bill amount",self.bill) 
            choose=int(input("Choose the Product:"))
            if(choose==1):
                Cosmetic_item={"Items":["1.Earings","2.Rings","3.Watches"],"Price":["200","100","500"],"Quantity":["20","30","40"]}            
                item1=Cosmetic_item["Items"]
                price1=Cosmetic_item["Price"]
                quantity1=Cosmetic_item["Quantity"]
                print(item1)
                choose1=int(input("Select Product:"))
                if(choose1==1):
                    print(item1[0],price1[0],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price1[0])
                    print("Your total cost:",totalCost)
                elif(choose1==2):
                    print(item1[1],price1[1],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price1[1])
                    print("Your total cost:",totalCost)
                elif(choose1==3):
                    print(item1[2],price1[2],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price1[2])
                    print("Your total cost:",totalCost)
            elif(choose==2):
                Cosmetic_item={"Items":["1.Nivea","2.Dove","3.Yardley"],"Price":["650","400","550"],"Quantity":["20","30","40"]}            
                item2=Cosmetic_item["Items"]
                price2=Cosmetic_item["Price"]
                quantity2=Cosmetic_item["Quantity"]
                print(item2)
                choose2=int(input("Select Product:"))
                if(choose2==1):
                    print(item2[0],price2[0],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price2[0])
                    print("Your total cost:",totalCost)
                elif(choose2==2):
                    print(item2[1],price2[1],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price2[1])
                    print("Your total cost:",totalCost)
                elif(choose2==3):
                    print(item2[2],price2[2],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price2[2])
                    print("Your total cost:",totalCost)
            elif(choose==3):
                Cosmetic_item={"Items":["1.Foundation","2.Eyeliner","3.Lipstick"],"Price":["1200","150","600"],"Quantity":["20","30","40"]}            
                item3=Cosmetic_item["Items"]
                price3=Cosmetic_item["Price"]
                quantity3=Cosmetic_item["Quantity"]
                print(item3)
                choose3=int(input("Select Product:"))
                if(choose3==1):
                    print(item3[0],price3[0],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price3[0])
                    print("Your total cost:",totalCost)
                elif(choose3==2):
                    print(item3[1],price3[1],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price3[1])
                    print("Your total cost:",totalCost)
                elif(choose3==3):
                    print(item3[2],price3[2],)
                    total=int(input("No.of quantity you want:"))
                    totalCost= total*int(price3[2])
                    print("Your total cost:",totalCost)
            
            self.bill =self.bill + totalCost
            totalcost=self.bill 
            print("Updated bill",totalcost)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
               
            Continue=int(input("Want to continue the shopping 1.Yes/2.No:"))
            if Continue==1:
                self.select()
            else:
               Payment().payment(totalcost)