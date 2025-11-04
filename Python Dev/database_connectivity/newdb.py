import sqlite3 as s

con = s.connect("cravita.db")
cur = con.cursor()
cur.execute("create table fortune (id int(10),name varchar(20))")
con.commit()
con.close()