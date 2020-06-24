import turtle
import random
import copy
import sys


class Manager:
	def __init__(self, size):
		self.matrix = []
		self.create_matrix(size)

	def create_matrix(self, size):
		for y in range(size):
			row = []
			for x in range(size):
				if size % 2 == 0:
					if x < int(size / 2):
						row.append(random.randint(0, 1))
					else:
						row2 = copy.deepcopy(row)
						row.reverse()
						row = row2 + row
						break
				elif size % 2 == 1:
					if x <= int(size / 2):
						row.append(random.randint(0, 1))
					else:
						middlenumber = row.pop()
						row2 = copy.deepcopy(row)
						row.reverse()
						row = row2 + [middlenumber] + row
						break

			self.matrix.append(row)

	def put_turtle(self, size):
		x = 0
		for row in self.matrix:
			y = 0
			for column in row:
				if column == 1:
					print_turtle(x, y)
				y += 1
			x += 1


def print_turtle(x, y):
    printer.goto(y, x)
    printer.stamp()


colors = ['white', 'red', 'blue', 'lightgreen', 'yellow']
if len(sys.argv) != 2 or not sys.argv[1].isdigit():
	print('usage: avatar.py 20(or another number)')
	sys.exit()

size = int(sys.argv[1])
if size < 1:
	exit()

screensize = 500

screen = turtle.Screen()
screen.setup(screensize ,screensize, 500, 100)
screen.title('keyboard')
screen.bgcolor('black')
screen.setworldcoordinates(0, 0, size, size)

color = random.choice(colors)

printer = turtle.Turtle()
printer.shape('square')
printer.color(color)
printer.speed(0)
printer.penup()
print(printer.turtlesize())
printer.shapesize(23 / size , 23 / size)

manager = Manager(size)
manager.put_turtle(size)

turtle.done()