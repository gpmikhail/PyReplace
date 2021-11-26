import pandas as pd
import numpy as np
import random as r
import json
import ast
import glob
import os
from pathlib import Path
from shutil import copyfile

countCopy = int(input('Input desidered number of output copies: '))
rndY = float()
rndX = float()
rint_a = int(input('Random number a (ex. -3)'))
rint_b = int(input('Random number b (ex. 3)'))
print(rint_a, rint_b)


shdwCounter = len(glob.glob1("txtIn\\Profiles","*.profile"))
#print(shdwCounter)

for k in range (countCopy):
	Path("txtOut\\"+str(k+1)+"\\[H] 1-60 Grinding").mkdir(parents=True, exist_ok=True)
txIn = r'txtIn\\Profiles'
for filename in os.listdir(txIn):
	if filename.endswith(".profile"):
		print(os.path.join(filename))
		dirfile = txIn+"\\"+filename
		f = open(dirfile, 'r')
		string = f.read()
		cut1 = string.split('\"Hotspots\":')
		cut1[0] += '\"Hotspots\":'
		cut2 = cut1[1].split(']', 1)
		cut2[0] += ']'
		#print(cut2[0])
		hot = ast.literal_eval(cut2[0])
		#print(type(hot))
		ht_r = pd.DataFrame(hot)
		#print(ht)
		#print('Changed data')
		a = (len(ht_r.index))
		#print('Number of altered rows', (a))
		a = int(a)
		for l in range (countCopy):
			ht_w = pd.DataFrame(hot)
			#cut1w = '%s' % cut1[0]
			path = "txtOut\\"+str(l+1)+"\\[H] 1-60 Grinding"
			for i in range (a):
				rndY = r.random()
				rndX = r.random()
				ht_w.Y[i] = ("{:.8f}".format(ht_r.Y[i] + (r.randint(rint_a, rint_b) + rndY)))
				ht_w.X[i] = ("{:.8f}".format(ht_r.X[i] + (r.randint(rint_a, rint_b) + rndX)))
				roadRnd = r.randint(1, 9)
				#print("\n", "roadRnd = ", roadRnd)
				cut1w = cut1[0].replace("\"RoadPriority\":9,", "\"RoadPriority\":" + str(roadRnd) + ",")
				#print(cut1w)
				#print("X ", i, r.randint(rint_a, rint_b), rndX)
				#print("Y ", i, r.randint(rint_a, rint_b), rndY)
				result = ht_w.to_dict('results')
				js_2dict = json.dumps(result)
				outfile = path+"\\"+filename
				file = open(outfile, 'w')
				file.write(cut1w)
				file.write(js_2dict)
				file.write(cut2[1])
				file.close()
			else:
				f.close()
				continue