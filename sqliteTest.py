import sqlite3

with sqlite3.connect('Antena.db') as db:
#with sqlite3.connect('Fixa.db') as db:
    c = db.cursor()
#c.execute('create table if not exists RASPBERRY (RX text)')
c.execute('SELECT * FROM GYRO ORDER BY ACC_X DESC LIMIT 20')
rec = c.fetchall()
cont = 0
for item in rec:
	cont+=1
	print cont, item
db.commit()
c.close()
db.close()