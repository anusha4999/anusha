import sqlite3
con=sqlite3.connect('mydb')
con.execute('''CREATE TABLE batch
(id int PRIMARY KEY,f_name text not null,l_name text not null,address varchar(50));''')
con.close()