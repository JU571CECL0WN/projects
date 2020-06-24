import random

class Game:
	def __init__(self):
		self.players = {1: None, 2: None}
		self.winner = None
		self.current_player = None
		self.valid_numbers = [1, 2]
		self.pieces_left = 15
		self.default_pieces = 21

	def ready_for_play(self):
		return self.players[2] is not None and self.players[1] is not None

	def change_player(self):
		if self.current_player == 1:
			self.current_player = 2
		elif self.current_player == 2:
			self.current_player = 1

	def join_player(self, player_id):
		for space in self.players:
			if self.players[space] is None:
				self.players[space] = player_id
				break

	def leave(self, player_id):
		for space in self.players:
			if self.players[space] == player_id:
				self.players[space] = None
				break

	def start(self):
		if not self.current_player:
			self.current_player = random.choice(list(self.players.keys()))
			return True
		return False

	def finish(self):
		self.current_player = None
		self.leave(self.players[1])
		self.leave(self.players[2])
		self.pieces_left = self.default_pieces

	def take_pieces(self, number, player_id):
		if player_id == self.players.get(self.current_player):
			self.pieces_left -= number
			self.who_win()
			self.change_player()
			return True
		return False

	def who_win(self):
		if self.pieces_left < 1:
			self.winner = self.current_player
			self.finish()
