import random
from data.settings import total_players
from data.boxes.box_base import BoxBase


class CommunityChestBase(BoxBase):
	def __init__(self, position):
		self.name = 'Community Chest'
		super().__init__(position, self.name)
		self.cards = [attr for attr in dir(self) if '__' not in attr and attr.startswith('card_')]

	def choose_card(self):
		card = random.choice(self.cards)
		return getattr(self, card)

	def card_estate(self, player):
		sentence = 'State returns you. Receive 20 dollars'
		player.money += 20
		return sentence

	def card_inherit(self, player):
		sentence = 'You inherit 100 dollars'
		player.money += 100
		return sentence


	def card_bank_error(self, player):
		sentence = 'Banking error in your favor. receive 200 dollars'
		player.money += 200
		return sentence


	def card_advice_fees(self, player):
		sentence = 'Receive 25 dollars as advice fees'
		player.money += 25
		return sentence


	def card_hospital_bills(self, player):
		sentence = 'Pay hospital bills: 100 dollars'
		player.money -= 100
		return sentence


	def card_birthday(self, player):
		sentence = 'It\'s your birthday, recive 10 dollars of every player'
		for players in total_players:
			if players != player:
				players.money -= 10
				player.money += 10
		return sentence


	def card_shares_reports(self, player):
		sentence = 'The sale of your shares reports to you 50 dollars'
		player.money -= 50
		return sentence
