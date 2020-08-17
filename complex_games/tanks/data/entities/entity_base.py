import pygame
import random

class EntityBase(pygame.sprite.Sprite):
	def __init__(self, filename, init_position, speed):
		super().__init__()
		self.speed = speed
		self.alive = True

		self.image = pygame.image.load('C:\\Users\\Usuario\\Desktop\\Personal\\Python\\projects\\complex_games\\tanks\\data\\static\\{}'.format(filename)).convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(center=init_position)

	def move(self, x, y):
		self.rect.move_ip(x, y)

	def draw_range(self):
		pygame.draw.circle(screen, color, self.rect.center, self.range)


	def die(self):
		self.alive = False

	def get_position(self):
		return self.rect.center