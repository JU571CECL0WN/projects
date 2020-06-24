from data.boxes.box_base import BoxBase


class IncomeTax(BoxBase):
	def __init__(self):
		position = 4
		name = 'Income Tax'
		super().__init__(position, name)

	def use(self, player):
		player.money -= 200
