from DB_connection import query_execute, global_cursor, connection

query = "SHOW TABLES LIKE 'bank';"
result = query_execute(3, query, values=None)
if result is None:
    query = 'create table bank (s_no integer, bname varchar(30));'
    query_execute(5, query, values=None)
    data = [
        (1, 'State Bank Of India'), (2, 'Punjab National Bank'), (3, 'Indian Bank'),
        (4, 'Bank Of India'), (5, 'UCO Bank'), (6, 'Union Bank Of India'),
        (7, 'Central Bank Of India'), (8, 'Bank Of Baroda'), (9, 'Bank Of Maharashtra'),
        (10, 'Canara Bank'), (11, 'Punjab And Sind Bank'), (12, 'Indian Overseas Bank'),
        (13, 'ICICI Bank'), (14, 'HDFC Bank'), (15, 'Axis Bank'),
        (16, 'IDBI Bank'), (17, 'Dhanlaxmi Bank'), (18, 'Kotak Mahindra Bank'),
        (19, 'Federal Bank')
    ]
    query = "insert into bank values (%s,%s);"
    global_cursor.executemany(query, data)

# query = "insert into bank values (%i,%s);"
# query_execute(1, query, values=data)
