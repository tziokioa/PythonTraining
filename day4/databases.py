import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor2 = conn.cursor()
cursor.execute("Update phones set name = 'Police' where name = 'Hello'")
cursor2.execute("Select * from phones")
cursor2.close()
for record in cursor2.fetchall():
    print("Name: {}, Phone Number: {}".format(record[0],record[1]))

cursor.close()
try:
    cursor.execute("insert into phones values('Hello','911')")
except Exception as ex:
    print(str(ex))
for record in cursor2:
    print("Name: {}, Phone Number: {}".format(record[0],record[1]))