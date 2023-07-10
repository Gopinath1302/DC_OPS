import mysql.connector
connection = mysql.connector.connect(
        host="localhost",
        password="Vibhoo@123",
        user="root",
        database="Pharmadb"
    )
my_cursor=connection.cursor()
#my_cursor.execute("Create table User_Details(User_Name varchar(50),Email_Id varchar(255),Password varchar(255),Contact_Details varchar(255))")
#my_cursor.execute("drop table view__med")
#my_cursor.execute("Create table Sc_med (Medicine_Name varchar(255),Price numeric(10,2))")
#my_cursor.execute("Create table view__med (MedNamelist varchar(255),Price double)")
#my_cursor.execute("Create table PriceofAdded_med(MedNamelist varchar(255))")
# # # for i in my_cursor:
# # #   print (i)
