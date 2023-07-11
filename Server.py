import mysql.connector
db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Dharsana@06",
            database="application"
        )
cursor = db.cursor()
usertable="CREATE TABLE user (username varchar(20),phone_number varchar(10),password varchar(20))"

cursor.execute(usertable)
query="insert into user (username,password)values(%s,%s)"
values=("Devi","123*")
cursor.execute(query,values)

db.commit()
cursor.close()
db.close()