import mysql.connector
mydb = mysql.connector.connect(host="localhost" ,user="root",password="Selva@123",database="db1")

mycursor = mydb.cursor()
usertable="CREATE TABLE user (username varchar(20),password varchar(20))"
mycursor.execute(usertable)
query="insert into user (username,password)values(%s,%s)"
values=("Admin","Admin@123")
mycursor.execute(query,values)
mydb.commit()
mycursor.close()
mydb.close()