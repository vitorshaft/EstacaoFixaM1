from ftplib import FTP
ftp = FTP('192.168.43.167')
#ftp = FTP('192.168.0.23')
ftp.login('pi','123qwe')

ftp.cwd('/home/pi/FTP')
#file_name = '/FTP/teste.txt'
#ftp.storbinary('STOR ' + file_name, open(file_name, rb))
def grabFile():

    filename = 'Antena.db'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()
grabFile()
