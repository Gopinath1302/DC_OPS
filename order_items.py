from payments import Payments
import Database_Connection
from Database_Connection import connection,global_cursor
class Orderitems:

    @classmethod
    def orderitems(self,price,stock_ind,ind1):
        if ind1 == 0:
            query = "Select * from veg_details;"
            global_cursor.execute(query)
            result = global_cursor.fetchall()
            quantity = int(input("Enter Quantity\n"))
            # if quantity <= result[stock_ind-1][2]:
            #     balance = int(result[stock_ind-1][2])
            total_price = quantity*price
            print("price:",total_price)

            return total_price
                # balance -= quantity
                # name = result[stock_ind-1][0]
                # print(type(balance))
                # query = "update veg_details set stock = %d where (veg_name = %s and veg_price = %d)"
                # global_cursor.execute(query, (balance,name,price))
                # connection.commit()
                # Payments().paymentchoice()
            # else:
            #     print("out of stock")


        if ind1 == 1:
            query = "Select * from grocery_details;"
            global_cursor.execute(query)
            result = global_cursor.fetchall()
            quantity = int(input("Enter Quantity\n"))
            # if quantity <= result[stock_ind-1][2]:
            #     balance = int(result[stock_ind-1][2])
            total_price = quantity*price
            print("price:",total_price)

            return total_price
                # balance -= quantity
                # name = result[stock_ind-1][0]
                # Payments().paymentchoice()


        if ind1 == 2:
            query = "Select * from fruit_details;"
            global_cursor.execute(query)
            result = global_cursor.fetchall()
            quantity = int(input("Enter Quantity\n"))
            # if quantity <= result[stock_ind-1][2]:
            #     balance = int(result[stock_ind-1][2])
            total_price = quantity*price
            print("price:",total_price)
            
            return total_price
                # balance -= quantity
                # name = result[stock_ind-1][0]                
                # Payments().paymentchoice()  

  

           
     
  
        