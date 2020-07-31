def start(myTurtle, walls, finish, cellWidth):
	myTurtle.shape('circle')
	myTurtle.showturtle()
	visited = []

	def dfs_path(x, y, visited):
		
		if((x,y) in finish):
			myTurtle.pencolor('red')
			myTurtle.goto(x,y)
			return True

		if((x,y) not in walls and (x,y) not in visited):
			visited.append((x,y))
			
			myTurtle.pencolor('red')
			myTurtle.goto(x,y)
			myTurtle.pencolor('green')

			if(dfs_path(x-cellWidth, y, visited)):
				return True

			myTurtle.goto(x,y)

			if(dfs_path(x+cellWidth, y, visited)):
				return True

			myTurtle.goto(x,y)

			if(dfs_path(x, y-cellWidth, visited)):
				return True

			myTurtle.goto(x,y)

			if(dfs_path(x, y+cellWidth, visited)):
				return True
			
			myTurtle.goto(x,y)




	x = round(myTurtle.xcor(),1)
	y = round(myTurtle.ycor(),1)
	dfs_path(x, y, visited)



