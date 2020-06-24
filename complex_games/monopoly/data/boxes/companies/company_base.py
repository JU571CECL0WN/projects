from data.boxes.box_base import BoxBase

class CompanyBase(BoxBase):
	def __init__(self, position, name):
		super().__init__(position, name)
		self.owner = None
		self.price = 150

	def pay_company(self, player):
		if self.owner_companies() == 1:
			player.money -= player.dice_number * 4
			self.owner.money +=  player.dice_number * 4
		elif self.owner_companies() == 2:
			player.money -= player.dice_number * 10
			self.owner.money +=  player.dice_number * 10

	def owner_companies(self):
		result = 0
		for possession in self.owner.possessions:
			if isinstance(possession, CompanyBase):
				result += 1
		return result
		

	def set_owner(self, player):
		self.owner = player
		player.money -= self.price