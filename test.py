import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, user text, password text)"
cursor.execute(create_table)

user = (1, 'Jane', 'qwer')
insert_query = "Insert INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)

users = [
     (2, 'Tina', 'asdf'),
     (3, 'Lisa', 'zxcv')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print (row)

# if add datas
connection.commit()

connection.close()
