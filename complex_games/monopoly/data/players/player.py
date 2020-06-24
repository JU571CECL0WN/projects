from data import settings


class Player:
	def __init__(self, name, player_number):
		self.name = name
		self.player_number = player_number
		self.position = 0
		self.dice_number = 0
		self.money = settings.initial_money
		self.possessions = []
		self.cooldown = 0

	def add_possession(self, hotel):
		self.possessions.append(possession)

	def remove_possession(self, hotel):
		self.possessions.remove(possession)

	def move(self):
		if self.position <= 38:
			self.position += 1 
		else: 
			self.position = 0

	def get_money(self, money):
		self.money += money

	def lost_money(self, money):
		self.money -= money
		