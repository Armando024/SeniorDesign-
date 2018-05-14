#reinforcement learning
#0-24
def fill_dead_ends(maze):
 	#top down
 	for y in range(1,10):
 		left1 = -1
 		for x in range(0,24):
 			c = maze[y][x]
 			if c == 1 and (left1 == x-1 or left1 == -1):
 				left1 = x
 				# print("left1", y, left1)
 				continue

 			if c==1 and left1 != -1:
 				# print("right1",x)
 				deadend = True
 				for x1 in range(left1+1,x):
 					if(maze[y-1][x1] != 1):
 						deadend = False
 						break
 				# print("deadend",deadend)
 				if deadend:
 					for x1 in range(left1+1,x):
 						maze[y][x1] = 1

 				left1 = -1

 	#bottom up
 	for y in range(22,14,-1):
 		left1 = -1
 		for x in range(0,24):
 			c = maze[y][x]
 			if c == 1 and (left1 == x-1 or left1 == -1):
 				left1 = x
 				# print("left1", y, left1)
 				continue

 			if c==1 and left1 != -1:
 				# print("right1",x)
 				deadend = True
 				for x1 in range(left1+1,x):
 					if(maze[y+1][x1] != 1):
 						deadend = False
 						break
 				# print("deadend",deadend)
 				if deadend:
 					for x1 in range(left1+1,x):
 						maze[y][x1] = 1

 				left1 = -1


 	#left to right
 	for x in range(1,10):
 		left1 = -1
 		for y in range(0,24):
 			c = maze[y][x]
 			if c == 1 and (left1 == y-1 or left1 == -1):
 				left1 = y
 				# print("left1", x, left1)
 				continue

 			if c==1 and left1 != -1:
 				# print("right1",y)
 				deadend = True
 				for y1 in range(left1+1,y):
 					if(maze[y1][x-1] != 1):
 						deadend = False
 						break
 				# print("deadend",deadend)
 				if deadend:
 					for y1 in range(left1+1,y):
 						maze[y1][x] = 1

 				left1 = -1


	#left to right
 	for x in range(22,14,-1):
 		left1 = -1
 		for y in range(0,24):
 			c = maze[y][x]
 			if c == 1 and (left1 == y-1 or left1 == -1):
 				left1 = y
 				# print("left1", x, left1)
 				continue

 			if c==1 and left1 != -1:
 				# print("right1",y)
 				deadend = True
 				for y1 in range(left1+1,y):
 					if(maze[y1][x+1] != 1):
 						deadend = False
 						break
 				# print("deadend",deadend)
 				if deadend:
 					for y1 in range(left1+1,y):
 						maze[y1][x] = 1

 				left1 = -1




 			
 						

 	return maze


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

def copy_into(main, sub, yStart, xStart):
	for y in range(0,len(sub)):
		for x in range (0, len(sub[y])):
			if x+xStart < 0 or y+yStart < 0 or  y+yStart >= len(main) or x+xStart >= len(main[y]) :
				continue #don't copy if copy location is out of bounds

			main[y+yStart][x+xStart] = sub[y][x]

	return main

# test code
# m = sample_maze([[1,0,1],[0,0,0],[1,0,1]])
# for i in range(0,24):
# 	m[0][i] = 1
# 	m[i][0] = 1
# 	m[23][i] = 1
# 	m[i][23] = 1
# m1 = fill_dead_ends(m)
# for y in m1:
	# print(y)


