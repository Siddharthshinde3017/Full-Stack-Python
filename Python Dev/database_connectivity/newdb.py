import sqlite3 as s

con = s.connect("cravita.db")
cur = con.cursor()
# cur.execute("create table fortune (id int(10),name varchar(20))")
# cur.execute("insert into fortune(id,name) values(1,'Python') ")
# cur.execute("insert into fortune values(2,'sql')")
# cur.execute("delete from fortune where id = '2'")

# cur.execute("insert into fortune(id,name) values(?,?)",(3,'abc'))  #for flask we insert data in that way

# a = [(4,'Java'),(5,'sql'),(6,'js')]
# cur.executemany("insert into fortune(id,name) values(?,?)",a)

# data = cur.execute("select * from fortune")
#
# print(data)
# for row in data:
#     print(row)

cur.execute("select * from fortune where id = ?",[4])
data = cur.fetchone()
print(data)
con.commit()
con.close()