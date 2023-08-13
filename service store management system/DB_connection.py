# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 07/02/2023
# Last Modified Date : 07/08/2023
# Reviewed by        : Silpa Madhusoodanan
# Reviewed on        : 20/02/2023


import mysql.connector
import sys
import time


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="appdata"
)

global_cursor = connection.cursor()


# User defined function to check and create the necessary tables in DB if needed
def check_db():
    # Check for table credential
    query = "SHOW TABLES LIKE 'credentials';"
    result = query_execute(3, query, values=None)
    if not result:
        query = ('create table credentials (cus_id varchar(10), username varchar(20), password varchar(64), '
                 'phoneno varchar(10), emailid varchar(50), joindate date);')
        query_execute(5, query, values=None)
        data = ('ADMAd44674', 'Admin', 'e86f78a8a3caf0b60d8e74e5942aa6d86dc150cd3c03338aef25b7d2d7e3acc7', '4467404000',
                'admin-india@aspiresys.com', '2023-07-02')
        query = "insert into credentials values (%s, %s, %s, %s, %s, %s);"
        query_execute(1, query, data)

    # Check for  table userdata
    query = "SHOW TABLES LIKE 'userdata';"
    result = query_execute(3, query, values=None)
    if not result:
        query = ('create table userdata ( cus_id varchar(10), username varchar(30), fname varchar(20), lname varchar('
                 '20), dob date, emailid varchar(40), phone varchar(10), zip_code varchar(10), timestamp varchar(20));')
        query_execute(5, query, values=None)
        data = ('ADMAd44674', 'Admin', None, None, None, 'admin-india@aspiresys.com', '4467404000', None, '2023-07-02')
        query = "insert into userdata values (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        query_execute(1, query, data)

    # Check for table address
    query = "SHOW TABLES LIKE 'address';"
    result = query_execute(3, query, values=None)
    if not result:
        query = ('create table address( cus_id varchar(10), door_no varchar(5), street varchar(50), city varchar(30), '
                 'state varchar(20), country varchar(30), zip_code varchar(10), timestamp varchar(20));')
        query_execute(5, query, values=None)
        query = "insert into address values(%s, %s, %s, %s, %s, %s, %s, %s);"
        data = ('ADMAd44674', None, None, None, None, None, None, '2023-07-02')
        query_execute(1, query, data)

    # Check for table service
    query = "SHOW TABLES LIKE 'service';"
    result = query_execute(3, query, values=None)
    if not result:
        query = ('create table service ( cus_id varchar(10), service_id varchar(10), service_name varchar(20), '
                 'price int, sdate date, timestamp varchar(20), p_status varchar(10));')
        query_execute(5, query, values=None)

    # Check for table bank
    query = "SHOW TABLES LIKE 'bank';"
    result = query_execute(3, query, values=None)
    if not result:
        query = 'create table bank (s_no integer, bank_name varchar(30));'
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
        connection.commit()

# User-defined function to perform various query operations
def query_execute(case, query, values):
    result = None
    global_cursor.execute(query, values)
    # Case 1 and case 2  for insert and for update respectively
    if case == 1 or case == 2:
        connection.commit()
    # Case 3 for select which return single row from DB
    elif case == 3:
        result = global_cursor.fetchone()
    # Case 4 for select which returns multiple rows from DB
    elif case == 4:
        result = global_cursor.fetchall()
    elif case == 5:
        result = global_cursor.fetchone()
    return result

# User-defined function to close the cursor and the connections
def close_db_connection():
    global_cursor.close()
    connection.close()


def loading_animation(case,word):
    animation_chars1 = ["[                   ]", "[█                  ]", "[██                 ]",
                        "[███                ]", "[████               ]", "[█████              ]",
                        "[██████             ]", "[███████            ]", "[████████           ]",
                        "[█████████          ]", "[██████████         ]", "[███████████        ]",
                        "[████████████       ]", "[█████████████      ]", "[██████████████     ]",
                        "[███████████████    ]", "[████████████████   ]", "[█████████████████  ]",
                        "[██████████████████ ]", "[███████████████████]", "complete!"]  # 21
    animation_chars2 = [ '.', '..', '...', '....', '.', '..', '...', '....', "complete!"]  # 9
    animation_chars3 = ['◜', ' ◝', ' ◞', '◟ ', '◠', '◡', '𐤏', "complete!"]  # 8
    animation_chars4 = ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚', "complete!"]  # 13
    animation_chars5 = ['◕', '◒', '◑', '◓', '◐', '◔', '◖', '◗', '●', "complete!"]  # 10
    animation_chars6 = ['⌜ ', ' ⌝', ' ⌟', '⌞ ', "complete!"]  # 5
    if word is None:
        word ='Loading'
    # 21 seconds
    if case == 1:
        for i in range(21):
            sys.stdout.write("\r" +word+" " + animation_chars1[i])
            sys.stdout.flush()
            time.sleep(1)
    # 6 seconds
    if case == 2:
        for i in range(9):
            sys.stdout.write("\r" + word+" "+ animation_chars2[i])
            sys.stdout.flush()
            time.sleep(.25)
    # 8 seconds
    if case == 3:
        for i in range(8):
            sys.stdout.write("\r" + word+" "+ animation_chars3[i])
            sys.stdout.flush()
            time.sleep(1)
    # 13 seconds
    if case == 4:
        for i in range(13):
            sys.stdout.write("\r" + word+" "+ animation_chars4[i])
            sys.stdout.flush()
            time.sleep(1)
    # 10 seconds
    if case == 5:
        for i in range(10):
            sys.stdout.write("\r" + word+" "+ animation_chars5[i])
            sys.stdout.flush()
            time.sleep(1)
    # 5 seconds
    if case == 6:
        for i in range(5):
            sys.stdout.write("\r" + word+" "+ animation_chars6[i])
            sys.stdout.flush()
            time.sleep(1)
    print("\n")
