import turtle                    # import turtle library
from turtle import *
import time
import sys
import random

import maze_generator

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.setup(1300,700)                  # setup the dimensions of the working window



width = random.randint(10,20)*2+1
height = random.randint(10,20)*2+1
print(width, height)
width = 9
height = 9
grid = maze_generator.createMaze(width,height)

cellWidth = row = int(min(700.0 / len(grid), 1300.0 / len(grid[0])) - 2)

# class for the Maze turtle (white square)
class Maze(turtle.Turtle):               # define a Maze class
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.visible = False
		self.penup()                    # lift up the pen so it do not leave a trail
		self.shape("square")            # the turtle shape
		self.color("white")             # colour of the turtle
		self.speed(10)                   # sets the speed that the #maze is written to the screen
		self.shapesize(cellWidth/24.0)

# class for the End marker turtle (green square)
class End(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.shape("square")
		self.color("green")
		self.speed(0)
		self.shapesize(cellWidth/24.0)

# class for the sprite turtle (red turtle)
class sprite(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		#self.penup()
		self.shape("turtle")
		self.color("red")
		self.setheading(270)  # point turtle to point down
		self.speed(0)
		self.shapesize(cellWidth/24.0)
		self.goto(100,100)

	def spriteDown(self):
		if (self.heading() == 270):                   # check to see if the sprite is pointing down
			x_walls = round(sprite.xcor(),0)          # sprite x coordinates =
			y_walls = round(sprite.ycor(),0)
			if (x_walls, y_walls) in finish:          # if sprite and the
				print("Finished")
				endProgram()
			if (x_walls +cellWidth, y_walls) in walls:          # check to see if they are walls on the left
				if(x_walls, y_walls -cellWidth) not in walls:   # check to see if path ahead is clear
					self.forward(cellWidth)
				else:
					self.right(90)
			else:
				self.left(90)
				self.forward(cellWidth)


	def spriteleft(self):
		if (self.heading() == 0):
			x_walls = round(sprite.xcor(),0)
			y_walls = round(sprite.ycor(),0)
			if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
				print("Finished")
				endProgram()
			if (x_walls, y_walls +cellWidth) in walls:       # check to see if they are walls on the left
				if(x_walls +cellWidth, y_walls) not in walls:
					self.forward(cellWidth)
				else:
					self.right(90)
			else:
				self.left(90)
				self.forward(cellWidth)


	def spriteUp(self):
		if (self.heading() == 90):
			x_walls = round(sprite.xcor(),0)
			y_walls = round(sprite.ycor(),0)
			if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
				print("Finished")
				endProgram()
			if (x_walls -cellWidth, y_walls ) in walls:  # check to see if they are walls on the left
				if (x_walls, y_walls + cellWidth) not in walls:
					self.forward(cellWidth)
				else:
					self.right(90)
			else:
				self.left(90)
				self.forward(cellWidth)

	def spriteRight(self):
		if (self.heading() == 180):

			x_walls = round(sprite.xcor(),0)
			y_walls = round(sprite.ycor(),0)
			if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
				print("Finished")
				endProgram()
			if (x_walls, y_walls -cellWidth) in walls:  # check to see if they are walls on the left
				if (x_walls - cellWidth, y_walls) not in walls:
					self.forward(cellWidth)
				else:
					self.right(90)
			else:
				self.left(90)
				self.forward(cellWidth)


def endProgram():
	wn.exitonclick()
	sys.exit()


def setupMaze(grid):
	for y in range(len(grid)):                       # select each line in the grid
		for x in range(len(grid[y])):                # identify each character in the line
			character = grid[y][x]                   # assign the grid reference to the variable character
			screen_x = -588 + (x * cellWidth)               # assign screen_x to screen starting position for x ie -588
			screen_y = 288 - (y * cellWidth)                # assign screen_y to screen starting position for y ie  288

			if character == "+":                     # if grid character contains an +
				maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
				maze.showturtle()
				maze.stamp() 
				walls.append((screen_x, screen_y))   # add coordinate to walls list

			if character == "e":                     # if grid character contains an e
				maze.goto(screen_x, screen_y)         # move turtle to the x and y location and
				maze.color('green')
				maze.stamp()
				maze.color('white')                          # stamp a copy of the turtle (green square) on the screen
				finish.append((screen_x, screen_y))  # add coordinate to finish list

			#if character == "s":                     # if the grid character contains an s
				#a,b = (screen_x, screen_y)
				#sprite.goto(screen_x, screen_y)      # move turtle to the x and y location

# ############ main program starts here  ######################


maze = turtle.Turtle(shape="square")
maze.hideturtle()
maze.penup()                    # lift up the pen so it do not leave a trail
maze.color('white')	
maze.speed(5)
maze.shapesize(cellWidth/24.0)

#sprite = sprite()            # enable the sprite  class
#time.sleep(1)

walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array

start = time.time()
setupMaze(grid)              # call the setup maze function
print("Time: " + str(time.time()-start))
while True:
		sprite.spriteRight()
		sprite.spriteDown()
		sprite.spriteleft()
		sprite.spriteUp()

		# time.sleep(0.02)

