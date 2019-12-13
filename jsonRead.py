import json

with open('Log.json') as json_file:
	data = json.load(json_file)
	for p in data['Log']:
		print p, "\n"
	
	#print data['Log']