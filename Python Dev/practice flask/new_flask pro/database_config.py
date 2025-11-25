import sqlite3

con = sqlite3.connect("real_estate.db")
c= con.cursor()
c.execute("create table admin(admin_id INTEGER PRIMARY KEY AUTOINCREMENT,username varchar(50) UNIQUE NOT NULL, password_hash varchar(255) NOT NULL,email varchar(100) UNIQUE NOT NULL, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
con.commit()
con.close()