import random
from data.entities.entity_base import EntityBase
from data import config
import math


class Enemy(EntityBase):
	def __init__(self):
		self.init_position = self.get_init()
		self.filename = 'enemy.png'
		self.init_speed = 5 
		super().__init__(self.filename, self.init_position, self.init_speed)

	def move_to_kill(self, player_position):
		x, y = self.get_position()
		destination = self.destination(player_position)
		if destination:
			self.move(destination[0], destination[1])

	def destination(self, player_position):
		player_x, player_y = player_position
		x, y = self.get_position()
		distance = math.sqrt(((player_x - x) ** 2) + ((player_y - y) ** 2))
		if distance == 0:
			return False
		n = distance / self.init_speed
		return ((player_x - x) / n,  (player_y - y) / n)

	def shoot(self):
		pass

	def get_init(self):
		list_ = [random.choice([0, config.SCREEN_SIZE[1]]), random.randint(0, config.SCREEN_SIZE[0])]
		random.shuffle(list_)
		return list_
