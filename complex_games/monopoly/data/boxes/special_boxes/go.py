from data.boxes.box_base import BoxBase


class Go(BoxBase):
	def __init__(self):
		position = 0
		name = 'Go'
		super().__init__(position, name)

	def use(self, player):
		player.money += 200