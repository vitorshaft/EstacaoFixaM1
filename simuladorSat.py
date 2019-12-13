import time
import math

N = 0.0
NNE = 22.5
NE = 45.0
ENE = 67.5
E = 90.0
SNE = 112.5
SE = 135.0
SSE = 157.5
S = 180.0
SSW = 202.5
SW = 225.0
WSW = 247.5
W = 270.0
WNW = 292.5
NW = 315.0
NNW = 337.5

#cada grau de longitude representa 100951.142 metros
#cada grau de latitude representa 110780.719 metros

lat0 = -23.484378
lat1 = -23.484378
lon0 = -47.487613
lon1 = -47.487613
alt0 = 0
alt1 = 0
velVentoKPH = 0.82
velVentoMPS = velVentoKPH/3.6
dirVento = SE
elapsed = 0

while alt1 < 30001:
	seno = math.sin(dirVento)
	cosseno = math.cos(dirVento)
	deltaLatS = (velVentoMPS/110780.719)*seno	#variacao de latitude por segundo em graus
	deltaLonS = (velVentoMPS/100951.142)*cosseno
	lat1 = lat0+deltaLatS
	lon1 = lon0+deltaLonS
	alt1 = alt0+5.833333
	

	posicao = open("cubeSatPos.txt","wb")
	posicao.write("%f,%f,%f"%(lat1,lon1,alt1))
	posicao.close()
	print lat1,lon1,alt1, elapsed, " s"
	time.sleep(1)
	lat0 = lat1
	lon0 = lon1
	alt0 = alt1
	elapsed = elapsed+1