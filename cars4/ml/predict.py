VISION_RADIUS = 24;
model_dir = './model5'


import tensorflow as tf
from random import uniform as random
import math 


def sample_maze(mazesub=[[1,0,1],[0,0,1],[1,0,1]]):
	mazescale = 8
	maze = []
	for y in range(0,len(mazesub)):
		for y2 in range(0,mazescale):
			maze.append([])
			for x in range(0, len(mazesub[y])):
				for x2 in range(0, mazescale):
					maze[-1].append(mazesub[y][x])

	return maze

def subArray(array, cy, cx, width, height):
		newArr = []
		for y in range(cy-math.floor(height/2),cy+math.ceil(height/2)):
			newArr.append([])
			for x in range(cx-math.floor(width/2),cx+math.ceil(width/2)):
				if y < 0 or y >= len(array) or x < 0 or x >= len(array[y]):
					newArr[-1].append(-1)
				else:
					newArr[-1].append(array[y][x])
		return newArr

def transpose(array):
	newArr = []
	for i in range(0,len(array)):
		newArr.append([0]*len(array))

	for y in range(0,len(array)):
		for x in range(0,len(array)):
			newArr[x][y] = array[y][x]
	return newArr

class Predictor:
	
	
	

	def __init__(self):
		self.stepsCount = 0
		self.lastInput = 0
		features = []
		# features.append(tf.feature_column.numeric_column("maze"));
		for x in range(0,VISION_RADIUS):
			for y in range(0,VISION_RADIUS):
				features.append(tf.feature_column.numeric_column(key=str(x)+"_"+str(y)))

		
		self.tfModel = tf.estimator.DNNClassifier(feature_columns=features,hidden_units=[20],model_dir=model_dir,n_classes=4)


	def input_fn(self, maze):
		features = {}
		for x in range(0,VISION_RADIUS):
			for y in range(0,VISION_RADIUS):
				if not str(x)+"_"+str(y) in features:
					features[str(x)+"_"+str(y)] = []
				features[str(x)+"_"+str(y)].append(maze[x][y])		

		return features


	def predict(self, maze):
		prediction = self.tfModel.predict(lambda: self.input_fn(maze))
		# print(list(tfModel.predict(input_fn)))
		# print(tfModel.predict(input_fn))
		
		probs = next(prediction)['probabilities']
		print(probs)
		return probs

	def act(self,maze):
		if self.stepsCount == 0:
			probs = self.predict(maze)

			for y in range(10,16):
				print(maze[y][10:16])

			if maze[10][12] == 1:		
				probs[0] = 0
			if maze[12][10] == 1:		
				probs[1] = 0
			if maze[14][12] == 1:		
				probs[2] = 0
			if maze[12][13] == 1:
				probs[3] = 0
			


			r = random(0,sum(probs))
			for i in range(0,len(probs)):
				if r < probs[i] :
					self.lastInput = i
					break
				else:
					r = r-probs[i]
			
			for y in maze:
				print(y)

			print(probs)

	
       			 

		self.stepsCount = self.stepsCount+1

		if self.stepsCount == 3:
			self.stepsCount = 0

		return self.lastInput

		