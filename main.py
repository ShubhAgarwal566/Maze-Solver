import turtle                    # import turtle library
from turtle import *
import time
import sys
import random

import maze_generator
import LHR

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.setup(1300,700)                  # setup the dimensions of the working window


width = random.randint(10,20)*2+1
height = random.randint(10,20)*2+1
print(width, height)
width = height = 9
grid = maze_generator.createMaze(width,height)

cellWidth = row = int(min(700.0 / len(grid), 1300.0 / len(grid[0])) - 2)

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

	
# ############ main program starts here  ######################


maze = turtle.Turtle(shape="square")
maze.hideturtle()
maze.penup()                    # lift up the pen so it do not leave a trail
maze.color('white')	
maze.speed(0) # fastest
maze.shapesize(cellWidth/24.0)

walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array
start = time.time()
setupMaze(grid)
print("End: " + str(time.time()-start))

myTurtle = turtle.Turtle(shape='turtle')
myTurtle.hideturtle()
myTurtle.color('red')
myTurtle.speed(5)
myTurtle.penup()
ratio = cellWidth/24.0
myTurtle.shapesize(cellWidth/24.0)
myTurtle.goto(-588+cellWidth, 288-cellWidth)
myTurtle.showturtle()
myTurtle.pendown()

LHR.start(myTurtle, walls, finish, cellWidth)
