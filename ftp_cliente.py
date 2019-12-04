from ftplib import FTP
ftp = FTP('xxx.xxx.xxx.xxx')	#inserir IP do Raspberry

ftp.login('login','senha')		#inserir login/senha de usuario (usar os do root se quiser)

ftp.cwd('/home/pi/FTP')
#file_name = '/FTP/teste.txt'
#ftp.storbinary('STOR ' + file_name, open(file_name, rb))
def grabFile():

    filename = 'arquivo.extensao'	#inserir arquivo a ser baixado

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()
grabFile()
