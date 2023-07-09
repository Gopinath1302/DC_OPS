import mysql.connector
db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gopinath2002.",
            database="rgbookstore"
        )
cursor = db.cursor()