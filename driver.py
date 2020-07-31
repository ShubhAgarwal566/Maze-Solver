import turtle                    
import Tkinter as tk

import maze_generator
import LHR
import randomMouse
import dfs

def start(width, height, speed, algo):

	maze_color = 'white'
	bg_color = 'black'

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

				elif character == "e":                     # if grid character contains an e
					maze.goto(screen_x, screen_y)         # move turtle to the x and y location and
					maze.color('green')
					maze.stamp()
					maze.color(maze_color)                          # stamp a copy of the turtle (green square) on the screen
					finish.append((screen_x, screen_y))  # add coordinate to finish list

		
	# ############ main program starts here  ######################

	
	grid = maze_generator.createMaze(width,height)
	cellWidth = row = int(min(700.0 / len(grid), 1300.0 / len(grid[0])) - 2)

	window = tk.Tk()
	window.title("Maze-Solver")
	window.geometry('1300x700')
	window.resizable(False, False)
	wn = turtle.Canvas(window, width=1300, height=700)
	wn.place(x=0, y=0)


	maze = turtle.RawTurtle(wn)
	wn['bg'] = bg_color
	maze.shape('square')
	maze.hideturtle()
	maze.penup()
	maze.color(maze_color)	
	maze.speed(0) # fastest
	maze.shapesize(cellWidth/24.0)


	walls =[]                    
	finish = []  
	setupMaze(grid)


	myTurtle = turtle.RawTurtle(wn)
	myTurtle.shape('turtle')
	myTurtle.hideturtle()
	myTurtle.color('red')
	myTurtle.speed(0)
	myTurtle.penup()
	ratio = cellWidth/24.0
	myTurtle.shapesize(cellWidth/24.0)
	myTurtle.goto(-588+cellWidth, 288-cellWidth)
	myTurtle.speed(speed)
	myTurtle.pendown()

	if(algo == 'Left Hand Rule'):
		LHR.start(myTurtle, walls, finish, cellWidth)
	elif(algo == 'Random Mouse'):
		randomMouse.start(myTurtle, walls, finish, cellWidth)
	elif(algo == 'Depth First Search'):
		dfs.start(myTurtle, walls, finish, cellWidth)
	#window.destroy()
	window.mainloop() # prevents program from quiting 


