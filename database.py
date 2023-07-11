import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="mysql@1",database="database")

mycursor = mydb.cursor()

usertable="CREATE TABLE user (username varchar(20),phone_number varchar(10),password varchar(20))"

mycursor.execute(usertable)
query="insert into user (username,phone_number,password)values(%s,%s,%s)"
values=("Admin","9080706050","Admin@123")
mycursor.execute(query,values)

mydb.commit()
mycursor.close()
mydb.close()
