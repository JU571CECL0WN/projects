from data.boxes.box_base import BoxBase

class Parking(BoxBase):
	def __init__(self):
		position = 20
		name = 'Parking'
		super().__init__(position, name)

	def use(self, player):
		pass
