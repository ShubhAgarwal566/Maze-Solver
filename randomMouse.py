import random

def start(myTurtle, walls, finish, cellWidth):
	endFlag = False
	while(endFlag==False):
		x = round(myTurtle.xcor(),0)
		y = round(myTurtle.ycor(),0)
		options = []

		if((x,y) in finish):
			endFlag = False
			break

		if(myTurtle.heading()==0): # facing right
			if((x+cellWidth,y) not in walls): #empty ahead
				options.append('f')
			if((x,y+cellWidth) not in walls): #empty on left
				options.append('l')
			if((x, y-cellWidth) not in walls): # empty on right
				options.append('r')
		elif(myTurtle.heading()==90): # facing up
			if((x,y+cellWidth) not in walls): #empty ahead
				options.append('f')
			if((x-cellWidth,y) not in walls): #empty on left
				options.append('l')
			if((x+cellWidth, y) not in walls): # empty on right
				options.append('r')
		elif(myTurtle.heading()==180): # facing left
			if((x-cellWidth,y) not in walls): #empty ahead
				options.append('f')
			if((x,y-cellWidth) not in walls): #empty on left
				options.append('l')
			if((x, y+cellWidth) not in walls): # empty on right
				options.append('r')
		elif(myTurtle.heading()==270): # facing down
			if((x,y-cellWidth) not in walls): #empty ahead
				options.append('f')
			if((x+cellWidth,y) not in walls): #empty on left
				options.append('l')
			if((x-cellWidth, y) not in walls): # empty on right
				options.append('r')

		if(len(options)==0):
			myTurtle.right(180)
		else:
			choice = random.choice(options)
			if(choice=='f'):
				myTurtle.forward(cellWidth)
			elif(choice=='l'):
				myTurtle.left(90)
				myTurtle.forward(cellWidth)
			elif(choice=='r'):
				myTurtle.right(90)
				myTurtle.forward(cellWidth)
		