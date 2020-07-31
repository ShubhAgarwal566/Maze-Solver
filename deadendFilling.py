from collections import deque


def wallCount(walls, filled, x, y, cellWidth):
	left = (x-cellWidth, y)
	right = (x+cellWidth, y)
	up = (x, y+cellWidth)
	down = (x, y-cellWidth)

	count = 0
	if(left in walls):
		count+=1
	if(right in walls):
		count+=1
	if(up in walls):
		count+=1
	if(down in walls):
		count+=1
	
	fillCount = 0
	if(left in filled):
		fillCount+=1
	if(right in filled):
		fillCount+=1
	if(up in filled):
		fillCount+=1
	if(down in filled):
		fillCount+=1

	return count, fillCount

def start(myTurtle, walls, finish, cellWidth, maze):
	
	q = deque()
	visited = []
	filled = []
	deadendList = []
	x = myTurtle.xcor()
	y = myTurtle.ycor()
	q.append((x,y))
	
	while (True):
		if(len(q)==0):
			break

		x,y = q.popleft()
		left = (x-cellWidth, y)
		right = (x+cellWidth, y)
		up = (x, y+cellWidth)
		down = (x, y-cellWidth)
		
		if(left not in walls and left not in visited):
			q.append(left)
		if(right not in walls and right not in visited):
			q.append(right)
		if(up not in walls and up not in visited):
			q.append(up)
		if(down not in walls and down not in visited):
			q.append(down)
		visited.append((x,y))

		if(wallCount(walls, filled, x, y, cellWidth)[0]==3 and (x,y) not in finish):
			deadendList.append((x,y))

	maze.color('grey')
	visited = []
	filled = []
	finish.append((myTurtle.xcor(), myTurtle.ycor())) # adding the starting coordinate in finish to avoid blocking it
	for i in range (len(deadendList)):
		x,y = deadendList[i][0], deadendList[i][1]
		while(True):
			wall, fill = wallCount(walls, filled, x, y, cellWidth) 
			if( fill+wall==3 and (x,y) not in finish):
				visited.append((x,y))
				maze.goto(x, y)
				filled.append((x,y))
				maze.stamp()
				
				left = (x-cellWidth, y)
				right = (x+cellWidth, y)
				up = (x, y+cellWidth)
				down = (x, y-cellWidth)
				
				if(left not in walls and left not in visited):
					x, y = left[0], left[1]
				if(right not in walls and right not in visited):
					x, y = right[0], right[1]
				if(up not in walls and up not in visited):
					x, y = up[0], up[1]
				if(down not in walls and down not in visited):
					x, y = down[0], down[1]
			else:
				break
