import math
import time

a = 6378000 #raio equatorial em metros
b = 6357000 #raio polar em metros
c = 6371000 #raio medio da terra (nao e media aritmetica)
H = 1.5

#dH = math.sqrt((2*H*c)+(H**2))	#distancia do horizonte

def horizonte(h0,Rm):
	p1 = 2*float(h0)*float(Rm)
	p2 = float(h0)**2
	dH = math.sqrt(p1+p2)
	return dH

def R(latitude):
	radiano = math.radians(float(latitude))
	num = (((a**2)*math.cos(radiano))**2) + (((b**2)*math.sin(radiano))**2)
	den = ((a*math.cos(radiano))**2) + ((b*math.sin(radiano))**2)
	div = num/den
	raiz = math.sqrt(div)
	return raiz

def azimute(latAnt,longAnt,latSat,longSat):
	#FALTA TRATAR AS SINGULARIDADES: ANGULOS COM MESMAS TANGENTES
	latA = float(latAnt)
	longA = float(longAnt)
	latS = float(latSat)
	longS = float(longSat)

	deltaX = longS-longA
	deltaY = latS-latA
	tg = deltaX/deltaY
	Az = math.degrees(math.atan(tg))
	if deltaX < 0 and deltaY < 0:
		Az = Az+180
	elif deltaX < 0 and deltaY > 0:
		Az = Az+270
	elif deltaX > 0 and deltaY < 0:
		Az = Az+90
	return Az

def compensacao(d0,d1,Raio):
	R = float(Raio)
	d2 = float(d0)-float(d1)
	h1 = math.sqrt((d2**2)+(R**2)) - R
	return h1

def elevacao(latAnt,longAnt,latSat,longSat,alt):
	latA = float(latAnt)
	longA = float(longAnt)
	latS = float(latSat)
	longS = float(longSat)
	altS = float(alt)

	#cada grau de longitude representa 100951.142 metros
	#cada grau de latitude representa 110780.719 metros

	deltaX = (float(longSat)-float(longAnt))*100951.142
	deltaY = (float(latSat)-float(latAnt))*110780.719
	D = math.sqrt((deltaX**2)+(deltaY**2))
	#D = 70000.0
	#Distancia = dist(latA,longA,latS,longS)
	hor = horizonte(H,R(latA))
	raio = R(latS)
	h1 = altS-compensacao(D,hor,raio)
	tg = h1/D

	El = math.degrees(math.atan(tg))

	return El, D

'''
lat = raw_input("Entre com a latitude (antena): \n")
lon = raw_input("Entre com a longitude (antena): \n")

latS = raw_input("Entre com a latitude (satelite): \n")
lonS = raw_input("Entre com a longitude (satelite): \n")
'''
lat = -23.483056
lon = -47.486389
'''
latS = -23.481520
lonS = -47.466527
altS = 30000.0
'''
arquivo = open("cubeSatPos.txt","r")
SAT = arquivo.read()
SAT = SAT.split(',')
for item in range(3):
	SAT[item] = float(SAT[item])
latS = SAT[0]
lonS = SAT[1]
altS = SAT[2]

dist = 70000
raio = R(lat)
horiz = horizonte(H,R(lat))
El = elevacao(lat,lon,latS,lonS,altS)
#X = dist(23,47,23,48)
while True:
	try:
		arquivo = open("cubeSatPos.txt","r")
		SAT = arquivo.read()
		SAT = SAT.split(',')
		for item in range(3):
			SAT[item] = float(SAT[item])

		latS = SAT[0]
		lonS = SAT[1]
		altS = SAT[2]
		print "Raio terrestre no local: ", raio, " m"
		print "Azimute: ",azimute(lat,lon,latS,lonS), " graus"
		print compensacao(elevacao(lat,lon,latS,lonS,altS)[1],horiz,raio), "metros de diferenca"
		print "distancia do horizonte: ", horiz
		print "elevacao e distancia: ",elevacao(lat,lon,latS,lonS,altS)[0], "graus; ",elevacao(lat,lon,latS,lonS,altS)[1],"metros"
		print SAT
	except:
		pass
	time.sleep(1)
	#print dist(lat,lon,latS,lonS)
