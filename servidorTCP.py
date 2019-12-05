import socket
import sqlite3

TCP_IP = 'xxx.xxx.xxx.xxx' # Atualizar o IP do PC quando necessario

TCP_PORT = 5005
BUFFER_SIZE = 20 # Normalmente 1024. 20 e para resposta rapida.

with sqlite3.connect('Fixa.db') as db:
    c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS RASPBERRY (A text)') #Tabela com apenas uma coluna
db.commit()
c.close()
db.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = 2, socket.SOCK_STREAM = 1
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
a = open("conexaoTCP.txt","w+")
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
    a.write(data)
    
    with sqlite3.connect('Fixa.db') as db:
    	c = db.cursor()
        c.execute('INSERT INTO RASPBERRY VALUES(?)',data[0])	#,?,?,?,?,?,?,?,?,?,?,?,?
        db.commit()
        c.execute('SELECT * FROM RASPBERRY')
        rec = c.fetchone()
        print rec
        db.commit()

a.close()
conn.close()
c.close()
db.close()
