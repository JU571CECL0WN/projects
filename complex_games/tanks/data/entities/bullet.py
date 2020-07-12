from data.entities.entity_base import EntityBase
import math


class Bullet(EntityBase):
	def __init__(self, owner, enemy):
		self.owner = owner
		self.init_position = owner.get_position()
		self.filename = 'bullet.png'
		self.image_frame = None
		self.speed = 10
		super().__init__(self.filename, self.init_position, self.speed)


	def move_to_kill(self, enemy_position):
		destination = self.destination(enemy_position)
		if destination:
			self.move(destination[0], destination[1])


	def destination(self, enemy_position):
		enemy_x, enemy_y = enemy_position
		x, y = self.init_position
		distance = math.sqrt(((enemy_x - x) ** 2) + ((enemy_y - y) ** 2))
		if distance == 0:
			return False 
		n = distance / self.speed
		return ((enemy_x - x) / n,  (enemy_y - y) / n)




