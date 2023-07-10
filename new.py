import mysql.connector

def create_table():
    conn = mysql.connector.connect(
       host="localhost" ,user="root",password="Selva@123",database="db1")

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dinner ( item VARCHAR(255),price DECIMAL(10, 2))
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_values(item, price):
    conn = mysql.connector.connect(
        host="localhost" ,user="root",password="Selva@123",database="db1")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Dinner (item, price) VALUES (%s, %s)', (item, price))
    conn.commit()
    cursor.close()
    conn.close()

create_table()
for i in range(4):
    item = input('Enter the item name: ')
    price = float(input('Enter the item price: '))
    insert_values(item, price)