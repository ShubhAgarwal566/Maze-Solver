def start(myTurtle, walls, finish, cellWidth):
	myTurtle.shape('circle')
	myTurtle.showturtle()
	path = []
	visited = []

	def dfs_path(x, y, path, visited):
		if((x,y) in finish):
			path.append((x,y))
			myTurtle.goto(x,y)
			return True

		if((x,y) not in walls and (x,y) not in visited):
			visited.append((x,y))
			myTurtle.goto(x,y)

			if(dfs_path(x-cellWidth, y, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)

			if(dfs_path(x+cellWidth, y, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)

			if(dfs_path(x, y-cellWidth, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)

			if(dfs_path(x, y+cellWidth, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)
			

	x = round(myTurtle.xcor(),1)
	y = round(myTurtle.ycor(),1)
	dfs_path(x, y, path, visited)



