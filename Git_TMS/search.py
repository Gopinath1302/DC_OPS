from payment1 import Payment
import db_connect
from db_connect import mydb, myobject 
import time
class Search:
    def place (self):
       print("_"*50,"Welcome to Vacation","_"*50)
       time.sleep(1)
       print("\n1. Hill station")
       print("2. Beach Areas")
       print("3. Historical places")
       flag=True
       while flag:
            try:
               choice=int(input("\tEnter your choice:\t"))
            except:
                print("_"*50,"Invalid choice","_"*50)
            else:
                flag=False
                if choice==1:
                    print("_"*50,"_"*50)
                    myobject.execute("select * from place_details1;")
                    result=myobject.fetchall()
                    for i in result:
                        print(i)
                        continue
                    print("_"*50,"_"*50)
                    Id=int(input("\n\tEnter hotel id:\t"))
                    package=int(input("\tEnter the number of package :\t"))  
                    Query=("select * from place_details1 where Id= %s ")
                    myobject.execute(Query,(Id,))
                    result1=myobject.fetchone()                     
                    amount = int(result1[4])                 
                    # sum=int(amount)
                    # print(type(package))
                    # print(type(amount))
                    # print(type(result1))
                    # print(type(result[4]))
                    Total_price = package * amount
                    print("\tTotal_price:",Total_price)
                    # print(type(Total_price))
                    print("_"*50,"_"*50)
                    print("\n")
                    Payment().paymentmethod()
                elif choice==2:
                    print("_"*50,"_"*50)
                    myobject.execute("select * from place_details2 ")
                    result=myobject.fetchall()
                    for i in result:
                        print(i)
                        continue
                    print("_"*50,"_"*50)
                    Id=int(input("\t\nEnter hotel id:\t"))
                    package=int(input("\tEnter the number of package:\t"))  
                    Query=("select * from place_details2 where Id= %s ")
                    myobject.execute(Query,(Id,))
                    result1=myobject.fetchone()                     
                    amount = int(result1[4])
                    Total_price =amount * package
                    # print("\tTotal_price:\t")
                    print("\tTotal_price:",Total_price)
                    print("_"*50,"_"*50)
                    print("\n")
                    Payment().paymentmethod()   
                elif choice==3:
                    print("_"*50,"_"*50)
                    myobject.execute("select * from place_details3;")
                    result=myobject.fetchall()
                    for i in result:
                        print(i)
                        continue
                    print("_"*50,"_"*50)
                    Id=int(input("\n\tEnter hotel id:\t"))
                    package=int(input("\tEnter the number of package :\t"))  
                    Query=("select * from place_details3 where Id= %s ")
                    myobject.execute(Query,(Id,))
                    result1=myobject.fetchone()                     
                    amount = int(result1[4])
                    Total_price =amount * package
                    print("\tTotal_price:",Total_price)
                    print("_"*50,"_"*50)
                    print("\n")
                    Payment().paymentmethod()    
                else:
                    flag=True
                    continue
           
            myobject.close()
            mydb.close()
                                





        