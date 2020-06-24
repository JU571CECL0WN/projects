import pygame
from pygame import locals
from data import map
import random

pygame.init()


size = 70
pixelpercell = 10
board = map.create_map(size)

while True:
	generations = input('Generations:')
	if generations.isdigit():
		generations = int(generations)
		break

while True:
	chances = input('Chances:(percent)')
	if chances.isdigit():
		chances = int(chances)
		chances = chances / 100
		break


screen_size = (size * pixelpercell, size * pixelpercell)
screen = pygame.display.set_mode(screen_size, 1, 32)
pygame.display.set_caption('Conway\'s Game of Life')


FPS = 40
fpsclock = pygame.time.Clock()
generations_2 = 0

for i in board:
	for j in i:
		if random.random() < chances:
			j.alive = 1


while True:
	for event in pygame.event.get():
		if event.type == locals.QUIT:
			pygame.quit()

	keystate = pygame.key.get_pressed()

	if generations == 0:
		continue

	if keystate[locals.K_SPACE]:
		cells_alive = 0
		for row in board:
			for cell in row:
				if cell.alive == 0:
					screen.blit(cell.image_false, (cell.x * pixelpercell, cell.y * pixelpercell))
				elif cell.alive == 1:
					screen.blit(cell.image_true, (cell.x * pixelpercell, cell.y * pixelpercell))
					cells_alive += 1
				cell.neighbour(board)
		for row in board:
			for cell in row:
				cell.change()

		generations -= 1
		generations_2 += 1

		pygame.display.set_caption('Conway\'s Game of Life - generations: {} cells_alive: {}'.format(generations_2, cells_alive))

	pygame.display.update()
	fpsclock.tick(FPS)