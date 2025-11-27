import bcrypt
import sqlite3



password = "admin@123"
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
hashed = hashed.decode("utf-8")

con = sqlite3.connect("real_estate.db")
cursor = con.cursor()
cursor.execute("""
insert into admin(username,password_hash, email)
values(?,?,?)""",("admin",hashed,"admin@gmail.com"))

con.commit()
con.close()
print("Admin user created successfully")

