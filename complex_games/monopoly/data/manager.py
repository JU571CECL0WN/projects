import pygame
import os
from pygame import locals
from data import settings 
from data.board import Board
from data.ui import UI
from data.players.player import Player
from data.utils import roll_dices
from data.boxes.chance.chance_base import ChanceBase
from data.boxes.community_chest.community_chest_base import CommunityChestBase
from data.boxes.companies.company_base import CompanyBase
from data.boxes.hotels.hotel_base import HotelBase
from data.boxes.trains.railroad_base import RailroadBase


class Manager:
	def __init__(self, number_players):
		self.players = []
		self.current_player = None
		self.number_players = number_players 
		self.init_players()
		self.board = Board()
		self.ui = UI()
		self.turns = 0
		self.text_font = pygame.font.SysFont('Arial', 30)
		self.colors = {
		'black': (0, 0, 0), 'white': (255, 255, 255), 'brown': (165, 42, 42),
		'pink': (255, 20, 147), 'orange': (255, 165, 0), 'red': (255, 0, 0),
		'yellow': (255, 255, 0), 'green': (0, 255, 0), 'blue':(0, 0, 255)
		}

	def init_players(self):
		for number in range(1, self.number_players + 1):
			name = input('name: ')
			player = Player(name, number)
			self.players.append(player)
			settings.total_players.append(player)


	def run(self):
		screen = self.ui.screen
		current_player_number = 1
		running = True

		while running:
			screen.blit(self.ui.background, (0 , 0))

			for event in pygame.event.get():
				if event.type == locals.QUIT:
					pygame.quit()


			if current_player_number == 5:
				current_player_number = 1

			for player in self.players:
				if player.player_number == current_player_number:
					current_player = player
					current_player.dice_number = 0
					movements = roll_dices()

					text = self.text_font.render('{}'.format(movements), False, self.colors['black'])
					screen.blit(text, (15, 15))

					for moves in range(movements):
						current_player.move()
						current_player.dice_number += 1

				screen.blit(self.ui.players_image[player.player_number], (self.ui.positions[player.position][0], self.ui.positions[player.position][1]))


			if isinstance(self.board.all_boxes[current_player.position], ChanceBase):
				card = self.board.all_boxes[current_player.position].choose_card()
				sentence = card(current_player)		# Xapuça
				text = self.text_font.render('{}'.format(sentence), False, self.colors['pink'])
				screen.blit(text, (10, 10))

			elif isinstance(self.board.all_boxes[current_player.position], CommunityChestBase):
				card = self.board.all_boxes[current_player.position].choose_card()
				sentence = card(current_player)		# Xapuça
				text = self.text_font.render('{}'.format(sentence), False, self.colors['pink'])
				screen.blit(text, (10, 10))

			elif isinstance(self.board.all_boxes[current_player.position], CompanyBase):
				if self.board.all_boxes[current_player.position].owner != None:
					self.board.all_boxes[current_player.position].pay_company(current_player)
				else:
					self.board.all_boxes[current_player.position].set_owner(current_player)
					current_player.possessions.append(self.board.all_boxes[current_player.position])

			elif isinstance(self.board.all_boxes[current_player.position], RailroadBase):
				if self.board.all_boxes[current_player.position].owner != None:
					self.board.all_boxes[current_player.position].pay_train(current_player)
				else:
					self.board.all_boxes[current_player.position].set_owner(current_player)
					current_player.possessions.append(self.board.all_boxes[current_player.position])

			elif isinstance(self.board.all_boxes[current_player.position], HotelBase):
				if self.board.all_boxes[current_player.position].owner != None:
					if self.board.all_boxes[current_player.position].owner == current_player:
						self.board.all_boxes[current_player.position].level_up()
					else:
						self.board.all_boxes[current_player.position].pay(current_player)
				else:
					self.board.all_boxes[current_player.position].set_owner(current_player)
					current_player.possessions.append(self.board.all_boxes[current_player.position])

			else:
				self.board.all_boxes[current_player.position].use(current_player)


			screen.blit(self.ui.players_image[current_player.player_number], (self.ui.positions[current_player.position][0], self.ui.positions[current_player.position][1]))

			current_player_number += 1
			pygame.display.update()
			self.ui.fpsclock.tick(self.ui.FPS)

			self.turns += 1

			for player in self.players:
				if player.money < 0:
					running = False
					pygame.quit()

		self.display_player_info()

		
	def display_player_info(self):
		os.system('cls')
		for player in self.players:
			print(player.name + ' - ' + str(player.money))
			for box in player.possessions:
				thing = box.name
				if hasattr(box, 'level'):
					thing += '  --  ' + str(box.level)
				print(thing)
			print('\n========================\n')
		print('This game has lasted for {}'.format(self.turns/self.number_players))
