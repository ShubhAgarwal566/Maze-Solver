def start(myTurtle, walls, finish, cellWidth):
	start.endFlag = False

	def goDown(myTurtle):
		if (myTurtle.heading() == 270):                   # check to see if the myTurtle is pointing down
			x_walls = round(myTurtle.xcor(),0)          # myTurtle x coordinates =
			y_walls = round(myTurtle.ycor(),0)
			if (x_walls, y_walls) in finish:          # if myTurtle and the
				#print("Finished")
				start.endFlag = True
			elif (x_walls +cellWidth, y_walls) in walls:          # check to see if they are walls on the left
				if(x_walls, y_walls -cellWidth) not in walls:   # check to see if path ahead is clear
					myTurtle.forward(cellWidth)
				else:
					myTurtle.right(90)
			else:
				myTurtle.left(90)
				myTurtle.forward(cellWidth)


	def goLeft(myTurtle):
		if (myTurtle.heading() == 0):
			x_walls = round(myTurtle.xcor(),0)
			y_walls = round(myTurtle.ycor(),0)
			if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
				#print("Finished")
				start.endFlag = True
			elif (x_walls, y_walls+cellWidth) in walls:       # check to see if they are walls on the left
				if(x_walls +cellWidth, y_walls) not in walls:
					myTurtle.forward(cellWidth)
				else:
					myTurtle.right(90)
			else:
				myTurtle.left(90)
				myTurtle.forward(cellWidth)


	def goUp(myTurtle):
		if (myTurtle.heading() == 90):
			x_walls = round(myTurtle.xcor(),0)
			y_walls = round(myTurtle.ycor(),0)
			if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
				#print("Finished")
				start.endFlag = True
			elif (x_walls -cellWidth, y_walls ) in walls:  # check to see if they are walls on the left
				if (x_walls, y_walls + cellWidth) not in walls:
					myTurtle.forward(cellWidth)
				else:
					myTurtle.right(90)
			else:
				myTurtle.left(90)
				myTurtle.forward(cellWidth)

	def goRight(myTurtle):
		if (myTurtle.heading() == 180):
			x_walls = round(myTurtle.xcor(),0)
			y_walls = round(myTurtle.ycor(),0)
			if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
				#print("Finished")
				start.endFlag = True
			elif (x_walls, y_walls -cellWidth) in walls:  # check to see if they are walls on the left
				if (x_walls - cellWidth, y_walls) not in walls:
					myTurtle.forward(cellWidth)
				else:
					myTurtle.right(90)
			else:
				myTurtle.left(90)
				myTurtle.forward(cellWidth)

	while(start.endFlag==False):
		if(not start.endFlag):
			goRight(myTurtle)
		if(not start.endFlag):
			goDown(myTurtle)
		if(not start.endFlag):
			goLeft(myTurtle)
		if(not start.endFlag):
			goUp(myTurtle)



