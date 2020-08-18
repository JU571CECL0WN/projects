from data.entities.entity_base import EntityBase
import math



class Bullet(EntityBase):
	def __init__(self, owner, enemy):
		self.owner = owner
		self.x, self.y = owner.get_position()
		self.filename = 'bullet.png'
		self.image_frame = None
		self.speed = 10
		self.enemy_x, self.enemy_y = enemy.get_position()
		self.destination = math.sqrt(((self.enemy_x - self.x) ** 2) + ((self.enemy_y - self.y) ** 2))
		super().__init__(self.filename, (self.x, self.y), self.speed)


	def flying(self):
		try:
			n = self.destination / self.speed
			destination = ((self.enemy_x - self.x) / n,  (self.enemy_y - self.y) / n)
			if destination:
				self.move(destination[0], destination[1])
		except ZeroDivisionError:
			pass

	def check_die(self, screen_size):
		position = self.get_position()
		if 0 > position[0] or 0 > position[1] or screen_size[0] < position[0] or screen_size[1] < position[1]:
			self.alive = False


