from order_items import Orderitems
from payments import Payments
import Database_Connection
from Database_Connection import connection,global_cursor

class Viewitems:
    @classmethod
    def viewitems(self):
        max_amt : int = 0
        bill_list = [] 
        index1 : int = 0
        flag = True
        while flag:
            print("\n")
            print("1 for vegitables")
            print("2 for grocery")
            print("3 for fruits")
            print("\n")
            user_choice = int(input("Enter Your Choice\n"))

            if user_choice == 1:
                print("  "*15+"Veg Section"+"  "*15)
                query = "Select * from veg_details;"
                global_cursor.execute(query)
                result = global_cursor.fetchall()
                print(result)
                print("1 for Carrot")
                print("2 for Potato")
                print("3 for Ladies finger")
                choice = int(input("Enter Your Choice:\n"))

                index = choice -1
                print(result[index][0],'\t\t\t\t',result[index][1],"per Kg")
                total_price = Orderitems.orderitems(result[index][1],choice,0)
                bill_list.append (result[index][0])
                bill_list.append (total_price)
                max_amt += total_price

                

            elif user_choice == 2:
                query = "Select * from grocery_details;"
                global_cursor.execute(query)
                result = global_cursor.fetchall()
                print(result)
                print("1 for Rice")
                print("2 for Dhal")
                print("3 for Oil")
                choice = int(input("Enter Your Choice:\n"))
                
                index = choice -1
                print(result[index][0],'\t\t\t\t',result[index][1],"per Kg")
                total_price = Orderitems.orderitems(result[index][1],choice,1)
                bill_list.append (result[index][0])
                bill_list.append (total_price)
                max_amt += total_price

            elif user_choice == 3:
                query = "Select * from fruit_details;"
                global_cursor.execute(query)
                result = global_cursor.fetchall()
                print(result)
                print("1 for Apple")
                print("2 for Orange")
                print("3 for Pomogranade")
                choice = int(input("Enter Your Choice:\n"))
                
                index = choice -1
                print(result[index][0],'\t\t\t\t',result[index][1],"per Kg")
                total_price = Orderitems.orderitems(result[index][1],choice,2)
                bill_list.append (result[index][0])
                bill_list.append (total_price)
                max_amt += total_price

            print("Do you want more to order?\t\t 1.Continue\t\t2.Goto Payments")
            user_option = int (input("Enter your Choice: "))
            if user_option == 1:
                flag = True
            elif user_option == 2 :
                for i in bill_list:
                    print(i)
                print("Your Total Amount Is :")
                print( max_amt)
                Payments().paymentchoice()
                flag = False

            # if choice == 1:                
            #     print("Price:",fruit_price[0])
            #     Orderitems.orderitems(fruit_price[0],0,2)
            # elif choice == 2:
            #     print("Price:",fruit_price[1])
            #     Orderitems.orderitems(fruit_price[1],0,2)
            # elif choice == 3:
            #     print("Price:",fruit_price[2])
            #     Orderitems.orderitems(fruit_price[2],0,2)
            # else:
            #     print("Out of Stock")