import math

def subArray(array, cx, cy, width, height):
	newArr = []
	for y in range(cy-math.floor(height/2),cy+math.ceil(height/2)):
		newArr.append([])
		for x in range(cx-math.floor(width/2),cx+math.ceil(width/2)):
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