import socket
import RPi.GPIO as GPIO
import time
import smbus			#import SMBus module of I2C
from time import sleep          #import

GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
  
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47


def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

def lerGyro():
	
	#Read Accelerometer raw value
	acc_x = read_raw_data(ACCEL_XOUT_H)
	acc_y = read_raw_data(ACCEL_YOUT_H)
	acc_z = read_raw_data(ACCEL_ZOUT_H)
	
	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Ax = acc_x/16384.0
	Ay = acc_y/16384.0
	Az = acc_z/16384.0
	

	#print ("Gx=%.2f" %Gx, "\tGy=%.2f" %Gy, "\tGz=%.2f" %Gz, "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
	#print "Ax = %.2f" %Ax
	#print "Ay = %.2f" %Ay
 	#print "Az = %.2f" %Az
	return [Ax,Ay,Az]
	

def subir(graus):
		GPIO.setmode(GPIO.BOARD)
		control_pins = [7,11,13,15]
		for pin in control_pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 0)
		
		fullstep_seq = [
			[1,1,0,0],
			[0,1,1,0],
			[0,0,1,1],
			[1,0,0,1]
		]
		passos = 2.667*graus
		for i in range(int(passos)):
			#for halfstep in range(8):	#maior precisao, menor velocidade
			for singlestep in range(4):	#maior velocidade, menor precisao
				
				for pin in range(4):
					GPIO.output(control_pins[pin], fullstep_seq[singlestep][pin])
					time.sleep(0.001)
		#frente(512)
		GPIO.cleanup()
def descer(graus):
		GPIO.setmode(GPIO.BOARD)
		control_pins = [7,11,13,15]
		for pin in control_pins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 0)
		
		fullstep_seq = [
			[1,1,0,0],
			[0,1,1,0],
			[0,0,1,1],
			[1,0,0,1]
		]
		passos = 2.667*graus
		for i in range(int(passos)):
			#for halfstep in range(8):	#maior precisao, menor velocidade
			for singlestep in range(4):	#maior velocidade, menor precisao
				
				for pin in range(4):
					GPIO.output(control_pins[pin], fullstep_seq[singlestep*(-1)][pin])
					time.sleep(0.001)
		#frente(512)
		GPIO.cleanup()
def mirar(a):
	angulos = lerGyro()
	ang = float(a)/100
	if ang < angulos[1]:
		subir(1)
	elif ang > angulos[1]:
		descer(1)
	else:
		pass
	print angulos[1], ang
	time.sleep(0.001)

def com(msg):
	TCP_IP = '192.168.43.95' # this IP of my pc. When I want raspberry pi 2`s as a client, I replace it with its IP '169.254.54.195'
	TCP_PORT = 5005
	BUFFER_SIZE = 1024

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(msg)
	data = s.recv(BUFFER_SIZE)
	s.close()

print ("received data:", data)

while True:
	mirar(40)
