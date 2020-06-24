from data.boxes.box_base import BoxBase


class LuxuryTax(BoxBase):
	def __init__(self):
		position = 35
		name = 'Luxury Tax'
		super().__init__(position, name)

	def use(self, player):
		player.money -= 100
