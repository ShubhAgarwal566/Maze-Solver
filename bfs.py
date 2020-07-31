from collections import deque

def start(myTurtle, walls, finish, cellWidth, maze):
	maze.color('grey')
	q = deque()
	visited = []
	x = myTurtle.xcor()
	y = myTurtle.ycor()
	path = {(x,y):None}
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
			path[left] = (x,y)
			if(left not in finish):
				maze.goto(left)
				maze.stamp()
		if(right not in walls and right not in visited):
			q.append(right)
			path[right] = (x,y)
			if(right not in finish):
				maze.goto(right)
				maze.stamp()
		if(up not in walls and up not in visited):
			q.append(up)
			path[up] = (x,y)
			if(up not in finish):
				maze.goto(up)
				maze.stamp()
		if(down not in walls and down not in visited):
			q.append(down)
			path[down] = (x,y)
			if(down not in finish):
				maze.goto(down)
				maze.stamp()


		visited.append((x,y))
	
	finalPath = [finish[0]]
	source = finish[0]
	while(True):
		source = path[source]
		if(source==None):
			break
		finalPath.append(source)

	myTurtle.shape('circle')
	myTurtle.showturtle()
	myTurtle.pensize(2)
		
	for i in range (len(finalPath)-1, -1, -1):
		myTurtle.goto(finalPath[i][0], finalPath[i][1])
	