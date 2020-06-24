from data.boxes.box_base import BoxBase

class GoToJail(BoxBase):
	def __init__(self):
		position = 30
		name = 'Go to jail'
		super().__init__(position, name)
		
	def use(self, player):
		player.cooldown = 3
		player.position = 10
