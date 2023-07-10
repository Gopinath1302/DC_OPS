import mysql.connector
connect = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="1234",
    database ="db_railway"
)
cursor = connect.cursor()