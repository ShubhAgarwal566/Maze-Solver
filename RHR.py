def start(myTurtle, walls, finish, cellWidth):
	start.endFlag = False
	myTurtle.showturtle()

	while(start.endFlag==False):
		x = round(myTurtle.xcor(),0)
		y = round(myTurtle.ycor(),0)
		heading = myTurtle.heading()

		if ((x, y) in finish):  
			break
		
		if(heading==0):
			if( (x, y-cellWidth) in walls ):       # check to see if they are walls on the left
				if( (x+cellWidth, y) not in walls):
					myTurtle.forward(cellWidth)
				else:
					myTurtle.left(90)
			else:
				myTurtle.right(90)
				myTurtle.forward(cellWidth)

		
		if(heading==90):
			if( (x+cellWidth, y) in walls ):       # check to see if they are walls on the left
				if( (x, y+cellWidth) not in walls):
					myTurtle.forward(cellWidth)
				else:
					myTurtle.left(90)
			else:
				myTurtle.right(90)
				myTurtle.forward(cellWidth)
		
		if(heading==180):
			if( (x, y+cellWidth) in walls ):       # check to see if they are walls on the left
				if( (x-cellWidth, y) not in walls):
					myTurtle.forward(cellWidth)
				else:
					myTurtle.left(90)
			else:
				myTurtle.right(90)
				myTurtle.forward(cellWidth)
		
		if(heading==270):
			if( (x-cellWidth, y) in walls ):       # check to see if they are walls on the left
				if( (x, y-cellWidth) not in walls):
					myTurtle.forward(cellWidth)
				else:
					myTurtle.left(90)
			else:
				myTurtle.right(90)
				myTurtle.forward(cellWidth)



