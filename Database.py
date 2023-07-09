import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="coe")

mycursor = mydb.cursor()

usertable="CREATE TABLE user (id INT auto_increment primary key,username varchar(20),email varchar(50),password varchar(20))"

mycursor.execute(usertable)
query="insert into user (username,email,password)values(%s,%s,%s)"
values=("Admin","admin@gmail.com","Admin@123")
mycursor.execute(query,values)

mydb.commit()
mycursor.close()
mydb.close()

