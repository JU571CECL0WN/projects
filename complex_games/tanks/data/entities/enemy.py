import random
from data.entities.entity_base import EntityBase
from data import config
import math


class Enemy(EntityBase):
	def __init__(self):
		self.init_position = self.get_init()
		self.filename = 'enemy.png'
		self.init_speed = 5
		self.atk_speed = 1
		self.atk_is_ready = True
		self.atk_cool_down = 0
		self.range = 210
		super().__init__(self.filename, self.init_position, self.init_speed)

	def move_to_kill(self, player_position):
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
		return (player_x - x) / n, (player_y - y) / n

	def shoot(self):
		if self.atk_is_ready:
			self.atk_is_ready = False
			self.atk_cool_down += 1 / self.atk_speed
			return True
		else:
			self.atk_cool_down -= 0.01
			if self.atk_cool_down <= 0:
				self.atk_cool_down = 0
				self.atk_is_ready = True
				return False

	def get_init(self):
		list_ = [random.choice([0, config.SCREEN_SIZE[1]]), random.randint(0, config.SCREEN_SIZE[0])]
		random.shuffle(list_)
		return list_
