import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="mysql@1",database="database")

mycursor = mydb.cursor()