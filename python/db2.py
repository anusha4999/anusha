import sqlite3
con=sqlite3.connect('mydb')
con.execute('''INSERT INTO batch(id,f_name,l_name,address)values(0001,'batsman','reddy','mal')''')
con.execute('''INSERT INTO batch(id,f_name,l_name,address)values(0002,'ironman','reddy','mal')''')
con.execute('''INSERT INTO batch(id,f_name,l_name,address)values(0003,'superman','reddy','mal')''')
con.execute('''INSERT INTO batch(id,f_name,l_name,address)values(0004,'superman','reddy','mal')''')
con.execute('''INSERT INTO batch(id,f_name,l_name,address)values(0004,'superman','reddy','mal')''')

con.commit()
a=con.execute('''SELECT * FROM batch''')
for i in a:
	print(i)
con.close()