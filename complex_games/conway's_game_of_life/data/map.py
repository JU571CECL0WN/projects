import pygame

pygame.init()


class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.alive = 0
		self.neighbours = 0
		self.image_false = pygame.image.load('data\\black.jpg')
		self.image_true = pygame.image.load('data\\white.jpg')

	def neighbour(self, board):
		self.neighbours = 0
		if self.x >= 1:
			self.neighbours += board[self.y][self.x - 1].alive
		if self.y < len(board) - 1:
			self.neighbours += board[self.y + 1][self.x].alive
		if self.x < len(board) - 1:
			self.neighbours += board[self.y][self.x + 1].alive
		if self.y >= 1:
			self.neighbours += board[self.y - 1][self.x].alive
		if self.x >= 1 and self.y >= 1:
			self.neighbours += board[self.y - 1][self.x - 1].alive
		if self.x < len(board) - 1 and self.y < len(board) - 1:
			self.neighbours += board[self.y + 1][self.x + 1].alive
		if self.x >= 1 and self.y < len(board) - 1:
			self.neighbours += board[self.y + 1][self.x - 1].alive
		if self.x < len(board) - 1 and self.y >= 1:
			self.neighbours += board[self.y - 1][self.x + 1].alive

	def change(self):
		if self.alive == 1 and self.neighbours > 3 or self.neighbours < 2 :
			self.alive = 0
		elif self.alive == 0 and self.neighbours == 3:
			self.alive = 1


def create_map(size):
	result = []
	result2 = []
	for y in range(size):
		result2 = []
		for x in range(size):
			cell = Cell(x, y)
			result2.append(cell)
		result.append(result2)

	return result
