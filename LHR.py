walls = None
finish = None
cellWidth = None

endFlag = False

def goDown(myTurtle):
	global endFlag
	if (myTurtle.heading() == 270):                   # check to see if the myTurtle is pointing down
		x_walls = round(myTurtle.xcor(),0)          # myTurtle x coordinates =
		y_walls = round(myTurtle.ycor(),0)
		if (x_walls, y_walls) in finish:          # if myTurtle and the
			print("Finished")
			endFlag = True
		if (x_walls +cellWidth, y_walls) in walls:          # check to see if they are walls on the left
			if(x_walls, y_walls -cellWidth) not in walls:   # check to see if path ahead is clear
				myTurtle.forward(cellWidth)
			else:
				myTurtle.right(90)
		else:
			myTurtle.left(90)
			myTurtle.forward(cellWidth)


def goLeft(myTurtle):
	global endFlag
	if (myTurtle.heading() == 0):
		x_walls = round(myTurtle.xcor(),0)
		y_walls = round(myTurtle.ycor(),0)
		if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
			print("Finished")
			endFlag = True
		if (x_walls, y_walls +cellWidth) in walls:       # check to see if they are walls on the left
			if(x_walls +cellWidth, y_walls) not in walls:
				myTurtle.forward(cellWidth)
			else:
				myTurtle.right(90)
		else:
			myTurtle.left(90)
			myTurtle.forward(cellWidth)


def goUp(myTurtle):
	global endFlag
	if (myTurtle.heading() == 90):
		x_walls = round(myTurtle.xcor(),0)
		y_walls = round(myTurtle.ycor(),0)
		if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
			print("Finished")
			endFlag = True
		if (x_walls -cellWidth, y_walls ) in walls:  # check to see if they are walls on the left
			if (x_walls, y_walls + cellWidth) not in walls:
				myTurtle.forward(cellWidth)
			else:
				myTurtle.right(90)
		else:
			myTurtle.left(90)
			myTurtle.forward(cellWidth)

def goRight(myTurtle):
	global endFlag
	if (myTurtle.heading() == 180):
		x_walls = round(myTurtle.xcor(),0)
		y_walls = round(myTurtle.ycor(),0)
		if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
			print("Finished")
			endFlag = True
		if (x_walls, y_walls -cellWidth) in walls:  # check to see if they are walls on the left
			if (x_walls - cellWidth, y_walls) not in walls:
				myTurtle.forward(cellWidth)
			else:
				myTurtle.right(90)
		else:
			myTurtle.left(90)
			myTurtle.forward(cellWidth)



def start(myTurtle, wallsList, finishList, cWidth):
	global cellWidth, walls, finish
	walls = wallsList
	finish = finishList
	cellWidth = cWidth	
	while(endFlag==False):
		goRight(myTurtle)
		goDown(myTurtle)
		goLeft(myTurtle)
		goUp(myTurtle)

		# time.sleep(0.02)

