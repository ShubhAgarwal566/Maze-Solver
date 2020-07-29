from tkinter import *
from tkinter.ttk import Combobox
import random

import maze


class MyWindow:
	def __init__(self, win):
		self.lb_algo = Label(win, text="Algorithm")
		self.lb_algo.place(x=70,y=50)

		self.algo=Combobox(win, values=['Left Hand Rule', 'Other'])
		self.algo.place(x=150, y=50)
		
		self.lb_rows = Label(win, text="Rows")
		self.lb_cols = Label(win, text="Cols")
		self.lb_rows.place(x=70,y=100)
		self.lb_cols.place(x=70,y=150)


		self.rows=Entry()
		self.cols=Entry()
		self.rows.place(x=150, y=100)
		self.cols.place(x=150, y=150)

		self.lb_speed = Label(win, text="Speed")
		self.lb_speed.place(x=70, y=200)
		
		self.speed=Combobox(win, values=['Slowest', 'Slow', 'Normal', 'Fast', 'Fastest'])
		self.speed.place(x=150, y=200)
		
		self.b1=Button(win, text='Visualize', command=self.visualize)
		self.b1.place(x=150, y=250)
	
	def visualize(self):
		algo = self.algo.get()
		rows = self.rows.get()
		cols = self.cols.get()
		speed = self.speed.get()

		if(rows == ''):
			rows = random.randint(10,20)*2+1
		else:
			rows = int(rows)
		
		if(cols==''):
			cols = random.randint(10,20)*2+1
		else:
			cols = int(cols)

		if(speed == ''):
			speed = 5
		elif(speed == 'Slowest'):
			speed = 1
		elif(speed == 'Slow'):
			speed = 3
		elif(speed == 'Normal'):
			speed = 5
		elif(speed == 'Fast'):
			speed = 10
		elif(speed == 'Fastest'):
			speed = 0

		if(algo == 'Left Hand Rule'):
			pass
			maze.start(rows, cols, speed)
	
window1=Tk()
mywin=MyWindow(window1)
window1.title('Maze Settings')
window1.geometry("400x500")
window1.mainloop()