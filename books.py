from server import db,cursor
from payment import pay
class bookS():
  def book_details(self):
    print("--------------------------------------------------")
    print("Enter 1 for Action")
    print("Enter 2 for Romance")
    print("Enter 3 for Science-Fiction")
    flag=True
    while flag:
      try:
        option=int(input("enter your option "))
      except ValueError:
         print("Enter Only Numbers")
      else:
        flag=False
        if option==1:
          query="SELECT * FROM books where genre='Action'"
          cursor.execute(query)
          result = cursor.fetchall()
        elif option==2:
          query="SELECT * FROM books where genre='Romance'"
          cursor.execute(query)
          result = cursor.fetchall()
        elif option==3:
          query="SELECT * FROM books where genre='Sci-Fic'"
          cursor.execute(query)
          result = cursor.fetchall()
        else:
          flag=True
          continue
        for row in result:
          print("\n")
          print("Book_name :",row[1],"| ","Author_name :",row[2],"| ","Genre :",row[3],"| ","Quantity :",row[4],"| ","Price :",row[5])
        for row in result:
          flag=True
          while flag:
            try:
             purchase=int(input("Enter the number of book you need 1st shows is 1 "))
             items=int(input("Enter number of books needed "))
            except ValueError:
                print("Enter Only Numbers")
            else:
              flag=False
              if purchase==1 and items<row[5]:
                print(items*row[5])
              elif purchase==2 and items<row[5]:
               print(items*row[5])
              elif purchase==3 and items<row[5]:
                print(items*row[5])
              elif purchase>3 or purchase<0 and items>row[5]:
                flag=True
                continue
              flag=False
          break
    pay.payment()
    cursor.close()
    db.close()