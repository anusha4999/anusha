import sqlite3
con=sqlite3.connect('mydb')
con.execute('''CREATE TABLE details
(id int PRIMARY KEY,f_name text not null,l_name text not null,address varchar(50));''')
con.execute('''INSERT INTO details(id,f_name,l_name,address)values(0001,'batsman','reddy','mal')''')
con.execute('''INSERT INTO details(id,f_name,l_name,address)values(0002,'ironman','reddy','mal')''')
con.execute('''INSERT INTO details(id,f_name,l_name,address)values(0003,'superman','reddy','mal')''')
con.commit()
a=con.execute('''SELECT * FROM details''')
x=next(a)
for i in len(x):
	print("details of:",i)
	print('_____________________________________')
	print("first name is:",f_name)
	print("last name is:",l_name)
	print("address is:",address)
	