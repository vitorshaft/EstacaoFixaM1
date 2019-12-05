import sqlite3
from time import sleep

while 1:
	with sqlite3.connect('GyroRT.db') as db:
		c = db.cursor()
	c.execute('SELECT * FROM GYRO')
	rec = c.fetchone()
	db.commit()
	c.close()
	db.close()
	print rec
	sleep(2)