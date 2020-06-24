class BoxBase:
	def __init__(self, position, name):
		self.position = position
		self.players = []
		self.name = name

	def add_player(self, player):
		self.players.append(player)

	def remove_player(self, player):
		self.players.remove(player)
