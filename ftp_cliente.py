from ftplib import FTP

ftp = FTP('xxx.xxx.xxx.xxx')
ftp.login('user','senha')

ftp.cwd('/home/pi/FTP')
#file_name = '/FTP/teste.txt'
#ftp.storbinary('STOR ' + file_name, open(file_name, rb))
def grabFile():

    filename = 'RT.json'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()
'''
while True:
	try:
		grabFile()
	except:
		pass
'''
grabFile()