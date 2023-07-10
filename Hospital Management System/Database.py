from __future__ import print_function
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Jay4prasanth@'
)
cur = mydb.cursor()

#print(mydb)
#cursor.execute("CREATE DATABASE hms")

try:
    '''pat = cur.execute("""CREATE TABLE Patient ( first_name VARCHAR(20) not null,
                                                last_name VARCHAR(20) not null,
                                                initial VARCHAR(3) not null,
                                                phone_number VARCHAR(10) not null primary key,
                                                username VARCHAR(20) not null,
                                                password VARCHAR(20) not null)""")
    doc = cur.execute("""CREATE TABLE Doctor(first_name VARCHAR(20) not null,
                                                last_name VARCHAR(20) not null,
                                                initial VARCHAR(3) not null,
                                                phone_number VARCHAR(10) not null primary key,
                                                username VARCHAR(20) not null,
                                                password VARCHAR(20) not null,
                                                specialist varchar(30) not null,
                                                available VARCHAR(5) not null)""")'''
    admin = cur.execute("""CREATE TABLE Admin ( first_name VARCHAR(20) not null,
                                                last_name VARCHAR(20) not null,
                                                initial VARCHAR(3) not null,
                                                phone_number VARCHAR(10) not null primary key,
                                                username VARCHAR(20) not null,
                                                password VARCHAR(20) not null)""")
    
except:  
    mydb.rollback()


'''sql="insert into admin(first_name,last_name,initial,phone_number,username,password)values(%s,%s,%s,%s,%s,%s)"
val=("jay","prasanth","s","7094834556","jack","Jay4prasanth@")
try:
    cur.execute(sql,val)
    mydb.commit()
except:
    mydb.rollback()'''

mydb.close()  