'''
def start(myTurtle, walls, finish, cellWidth):
	path = []
	visited = []
	def recur(x,y,path, visited):
		myTurtle.goto(x,y)



'''
def start(myTurtle, walls, finish, cellWidth):

	path = []
	visited = []

	def recur(x, y, path, visited):
		if((x,y) in finish):
			path.append((x,y))
			myTurtle.goto(x,y)
			return True

		if((x,y) not in walls and (x,y) not in visited):
			visited.append((x,y))
			myTurtle.goto(x,y)

			if(recur(x-cellWidth, y, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)

			if(recur(x+cellWidth, y, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)

			if(recur(x, y-cellWidth, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)

			if(recur(x, y+cellWidth, path, visited)):
				path.append((x,y))
				return True
			myTurtle.goto(x,y)
			

	x = round(myTurtle.xcor(),1)
	y = round(myTurtle.ycor(),1)
	recur(x, y, path, visited)



