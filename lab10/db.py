import sqlite3

import function

db_connection = sqlite3.connect("sqlite.db")
print(db_connection)

db_cursor = db_connection.cursor()
print(db_cursor)

query1 = "SELECT * FROM demo"
db_cursor.execute(query1)

print("Reading 1 row")
rows = db_cursor.fetchone()
print(rows)

print("Reading 3 rows")
rows = db_cursor.fetchmany(3)
for r in rows:
    print(r)

print("Reading all rows")
rows = db_cursor.fetchall()
for r in rows:
    print(r)
function.query_responder(db_cursor, "fetchall")

query2 = "INSERT INTO demo (Name, Hint) VALUES ('Test', 'Insert')"
db_cursor.execute(query2)
db_connection.commit()

id = int(input("Insert ID: "))
query3 = "SELECT * FROM demo WHERE ID > ?"
db_cursor.execute(query3)
function.query_responder(db_cursor, "fetchall")