import cx_Oracle #sqlite3
#conn=sqlite3.connect("gopas.sqlite")
conn=cx_Oracle.connect("gopas/gopas@10.2.21.34:1521/orcl")
cursor=conn.cursor()
cursor1=conn.cursor()
cursor1.execute("insert into phones values('Gopas','244556677')")
conn.commit()
cursor.execute("select * from phones")
for record in cursor.fetchall():
  print("Name : %s, phone number : %s" %(record[0],record[1]))
conn.close()
