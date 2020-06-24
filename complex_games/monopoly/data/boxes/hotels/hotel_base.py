from data.boxes.box_base import BoxBase


class HotelBase(BoxBase):
	def __init__(self, position, name, price, group, rental_price):
		super().__init__(position, name)
		self.price = price
		self.max_level = 5
		self.level = 1
		self.group = group
		self.owner = None
		self.rental_price = rental_price

	def set_owner(self, player):
		self.owner = player

	def level_up(self):
		if self.level < self.max_level:
			self.level += 1

	def level_down(self):
		if self.level > 1:
			self.level -= 1

	def level_full(self):
		self.level = self.max_level

	def level_down_to_min(self):
		self.level = 1

	def pay(self, player):
		cost = self.rental_cost()
		player.money -= cost
		self.owner.money += cost

	def rental_cost(self):
		return self.rental_price[self.level]


