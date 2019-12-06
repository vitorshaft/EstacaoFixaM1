import os
from time import sleep

while True:
	os.system('python ftp_cliente.py')
	sleep(1)
	os.system('python jsonRead.py')