import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Boomi@2002",
    database="Tourism"
)
myobject = mydb.cursor()
# myobject.execute("create table details(cust_name varchar(20),cust_phonenumber long,cust_password varchar(20),cust_emailId varchar(20))")
# myobject.execute("show tables")

# myobject.execute("SHOW DATABASES")
# for x in myobject:
#   print(x)
