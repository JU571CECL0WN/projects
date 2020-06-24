import pygame

class UI:
	def __init__(self):
		self.static_path = 'C:\\Users\\Usuario\\Desktop\\Personal\\Python\\Finished\\complex_games\\paper_scissors_rock\\data\\images\\'
		self.game_images = {
		'rock': pygame.image.load(self.static_path + 'rock.png'),
		'scissors': pygame.image.load(self.static_path + 'scissors.png'),
		'paper': pygame.image.load(self.static_path + 'paper.png')
		}

	