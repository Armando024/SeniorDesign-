VISION_RADIUS = 24;
model_dir = './model4'


import tensorflow as tf
features = []
# features.append(tf.feature_column.numeric_column("maze"));
for x in range(0,VISION_RADIUS):
	for y in range(0,VISION_RADIUS):
		features.append(tf.feature_column.numeric_column(key=str(x)+"_"+str(y)))

tfModel = tf.estimator.DNNClassifier(feature_columns=features,hidden_units=[20],model_dir=model_dir,n_classes=4)

mazesub = [[1,1,1],[0,0,1],[1,1,1]]
mazescale = 8
maze = []
for y in range(0,len(mazesub)):
	for y2 in range(0,mazescale):
		maze.append([])
		for x in range(0, len(mazesub[y])):
			for x2 in range(0, mazescale):
				maze[-1].append(mazesub[y][x])




def input_fn():
	features = {}
	for x in range(0,VISION_RADIUS):
		for y in range(0,VISION_RADIUS):
			if not str(x)+"_"+str(y) in features:
				features[str(x)+"_"+str(y)] = []
			features[str(x)+"_"+str(y)].append(maze[x][y])		

	return features

prediction = tfModel.predict(input_fn)
# print(list(tfModel.predict(input_fn)))
# print(tfModel.predict(input_fn))
print(maze)
print(next(prediction)['probabilities'])