import json

with open('gyroRT.json') as json_file:
	data = json.load(json_file)
	'''for p in data['gyro']:
		print p['cosseno']
	'''
	print data['gyro']