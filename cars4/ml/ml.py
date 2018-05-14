inputcsv = 'output/output.csv'
model_dir = './model5'
VISION_RADIUS = 24;

import math

def subArray(array, cx, cy, width, height):
	newArr = []
	for y in range(cy-math.floor(height/2),cy+math.ceil(height/2)):
		newArr.append([])
		for x in range(cx-math.floor(width/2),cx+math.ceil(width/2)):
			if y < 0 or y >= len(array) or x < 0 or x >= len(array[y]):
				newArr[-1].append(-1)
			else:
				newArr[-1].append(array[y][x])
	return newArr
# test for above function
# a = []
# for y in range(0,10):
# 	a.append([])
# 	for x in range(0,10):
# 		a[-1].append((y+x)%10)

# b = subArray(a,2,2,5,5)
# print(b)



#import trainng data
import csv
import ast

inputReader = csv.DictReader(open(inputcsv))
inputs = [];

for row in inputReader:
	inputs.append({})
	inputs[-1]['x'] = row['X']
	inputs[-1]['y'] = row['Y']
	inputs[-1]['maze'] = subArray(ast.literal_eval(row['Maze'][1:-1]), int(row['X']), int(row['Y']), VISION_RADIUS, VISION_RADIUS)#trims quotes
	inputs[-1]['keypress'] = row['KeyPress']
	#print(str(inputs[-1]['maze']))



import tensorflow as tf
features = []
# features.append(tf.feature_column.numeric_column("maze"));
for x in range(0,VISION_RADIUS):
	for y in range(0,VISION_RADIUS):
		features.append(tf.feature_column.numeric_column(key=str(x)+"_"+str(y)))

tfModel = tf.estimator.DNNClassifier(feature_columns=features,hidden_units=[20],model_dir=model_dir,n_classes=4)


tf.Variable(inputs[0]['maze'])

keys = {"119" : 0, "97":1, "115":2, "100":3}

# Train Model
def input_fn(inputs):
	features = {"maze":[]}
	labels = []
	i=1
	for row in inputs:
		kp = row['keypress']
		if not kp in keys:
			continue
		
		print(i, row['maze'],keys[kp])
		i =i+1;
		for x in range(0,VISION_RADIUS):
			for y in range(0,VISION_RADIUS):
				if not str(x)+"_"+str(y) in features:
					features[str(x)+"_"+str(y)] = []
				features[str(x)+"_"+str(y)].append(row['maze'][x][y])
		# features['maze'].append(row['maze'])
		#kp == w, a, s , d

		labels.append(keys[str(kp)])
		# labels.append([kp == 119, kp == 97, kp == 115, kp == 100])
	for x in range(0,VISION_RADIUS):
		for y in range(0,VISION_RADIUS):
			print(len(features[str(x)+"_"+str(y)]))
	return (features, labels)


tfModel.train(input_fn = lambda: input_fn(inputs), steps=100)