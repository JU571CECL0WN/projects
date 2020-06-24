from data.boxes.box_base import BoxBase


class RailroadBase(BoxBase):
	def __init__(self, position, name):
		super().__init__(position, name)
		self.owner = None
		self.price = 200
		
	def pay_train(self, player):
		player.money -= int(12.5 * 2 ** self.owner_trains())
		
	def owner_trains(self):
		result = 0
		for possession in self.owner.possessions:
			if isinstance(possession, RailroadBase):
				result += 1

		return result
		

	def set_owner(self, player):
		self.owner = player
		player.money -= self.price