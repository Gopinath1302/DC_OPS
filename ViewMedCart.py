from Order import OrderMed
from dbconnection import connection,my_cursor
class MedCart:
    def view_medcart(Medlist,Medprice):
        flag = True
        global check
        global length
        check = 0
        # length = len(str(Medprice))
        my_cursor.execute("Select * from View__med")
        result=my_cursor.fetchall()
        length =len(result)
        
        while flag :
            for i in range(len(result)):
                print ("For",result[i][0]," : Rs. ",(result[i][1]))
            print("*-----*-----*-----*-----*-----*")
            print("")      
            if check <= length:
                print("")
                k=int(input("Do you want to order the medicine??\n1.Yes/press any key to view medicines only numbers:"))     
                check +=1
                if k==1:  
                    i = int(input("Enter your choice:"))
                    i-=1              
                    OrderMed.ordermed(result[i],i)

            else:
                 flag = False


            
            
               
            



                




        
      

 