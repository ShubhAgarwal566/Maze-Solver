def start(myTurtle, walls, finish, cellWidth, maze):
	maze.color('grey')

	path = []
	visited = []

	def dfs_path(x, y, path, visited):
		
		if((x,y) in finish):
			path.append((x,y))
			return True

		if((x,y) not in walls and (x,y) not in visited):
			visited.append((x,y))
			maze.goto(x,y)
			maze.stamp()	
			if(dfs_path(x-cellWidth, y, path, visited)):
				path.append((x,y))
				return True

			if(dfs_path(x+cellWidth, y, path, visited)):
				path.append((x,y))
				return True

			if(dfs_path(x, y-cellWidth, path, visited)):
				path.append((x,y))
				return True

			if(dfs_path(x, y+cellWidth, path, visited)):
				path.append((x,y))
				return True

		
	x = round(myTurtle.xcor(),1)
	y = round(myTurtle.ycor(),1)
	dfs_path(x, y, path, visited)
	
	myTurtle.shape('circle')
	myTurtle.showturtle()
	myTurtle.pensize(2)
	for i in range(len(path)-1, -1, -1):
		myTurtle.goto(path[i])

	


