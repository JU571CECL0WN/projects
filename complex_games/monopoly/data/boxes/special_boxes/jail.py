from data.boxes.box_base import BoxBase

class Jail(BoxBase):
	def __init__(self):
		position = 10
		name = 'Jail'
		super().__init__(position, name)
		
	def use(self, player):
		for player in self.players:
			if player.cooldown < 0:
				if player.number == 1:
					return 44, 620
				elif player.number == 2:
					return 55, 620
				elif player.number == 3:
					return 44, 656
				elif player.number == 4:
					return 55, 656
			else: 
				if player.number == 1:
					return 14, 656
				elif player.number == 2:
					return 14, 676
				elif player.number == 3:
					return 44, 676
				elif player.number == 4:
					return 64, 656

