from data.entities.entity_base import EntityBase
from data import config


class Player(EntityBase):
	def __init__(self):
		self.init_position = (290, 290)
		self.filename = 'player.png'
		self.init_speed = 7
		super().__init__(self.filename, self.init_position, self.init_speed)
		self.possible_enemies = ['enemy.png', 'bullet.png']
		self.limit_x, self.limit_y = self.image_size()
		self.range = 300
		self.atk_speed = 2
		self.atk_cool_down = 0
		self.atk_is_ready = True

	def image_size(self):
		x = self.image.get_width()
		y = self.image.get_height()
		return (x / 2), (y / 2)

	def move_left(self):
		if self.rect.center[0] > self.limit_x:
			self.move(-self.speed, 0)

	def move_right(self):
		if self.rect.center[0] < config.SCREEN_SIZE[0] - self.limit_x:
			self.move(+self.speed, 0)

	def move_up(self):
		if self.rect.center[1] > self.limit_y:
			self.move(0, -self.speed)

	def move_down(self):
		if self.rect.center[1] < config.SCREEN_SIZE[1] - self.limit_y:
			self.move(0, +self.speed)

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
