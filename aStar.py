class Node():
	"""A node class for A* Pathfinding"""

	def __init__(self, parent=None, position=None, g=0, h=0, f=0):
		self.parent = parent
		self.position = position
		self.g = g
		self.h = h
		self.f = f

	def __eq__(self, other):
		return self.position == other.position


def start(myTurtle, walls, finish, cellWidth, maze):
	maze.color('grey')
	
	start = Node(None, (myTurtle.xcor(), myTurtle.ycor()))
	end = Node(None, finish[0])

	opened = []
	closed = []
	path = []

	opened.append(start)
	while(len(opened) > 0):
		current = opened[0]
		currIndex = 0
		for index, item in enumerate(opened):
			if item.f < current.f:
				current = item
				currIndex = index

		opened.pop(currIndex)
		closed.append(current)

		if(current == end):
			while(current != None):
				path.append(current.position)
				current = current.parent
			break

		children = []
		for neighbour in [(0, -1*cellWidth), (0, 1*cellWidth), (-1*cellWidth, 0), (1*cellWidth, 0)]: # Adjacent squares
			node_position = (current.position[0] + neighbour[0], current.position[1] + neighbour[1])
			if(node_position[0]>end.position[0] or node_position[1]<end.position[1]): #below end
				continue
			if(node_position[0]<start.position[0] or node_position[1]>start.position[1]): # above start 
				continue
			if node_position in walls:
				continue

			new_node = Node(current, node_position)
			children.append(new_node)

		for child in children:
			hasFlag = False
			for closed_node in closed:
				if(child == closed_node):
					hasFlag = True
					break
			if(hasFlag):
				continue

			child.g = current.g + 1
			child.h = ((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2)
			child.f = child.g + child.h
			if(child.position != end.position):
				maze.goto(child.position[0], child.position[1])
				maze.stamp()

			hasFlag = False
			for opened_node in opened:
				if(child == opened_node and child.g > opened_node.g):
					hasFlag = True
					break
			if(hasFlag):
				continue

			opened.append(child)

	myTurtle.shape('circle')
	myTurtle.showturtle()
	myTurtle.pensize(2)
	for i in range(len(path)-1, -1, -1):
		myTurtle.goto(path[i])