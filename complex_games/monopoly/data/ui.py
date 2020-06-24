import pygame
from data.settings import static_path

class UI:
	def __init__(self):
		self.background = pygame.image.load(static_path + 'board.png')
		self.FPS = 30
		self.fpsclock = pygame.time.Clock()
		self.screen_size = (700,700)
		self.screen = pygame.display.set_mode(self.screen_size, 1, 32)
		self.players_image = {
		1: pygame.image.load(static_path + 'blue_player.png'),
		2: pygame.image.load(static_path + 'red_player.png'),
		3: pygame.image.load(static_path + 'green_player.png'),
		4: pygame.image.load(static_path + 'yellow_player.png')
		}
		self.positions = {
		0: [656, 656],
		1: [583, 656],
		2: [524, 656],
		3: [466, 656],
		4: [408, 656],
		5: [349, 656],
		6: [291, 656],
		7: [233, 656],
		8: [175, 656],
		9: [117, 656],
		10: [44, 656],
		11: [44, 583],
		12: [44, 524],
		13: [44, 466],
		14: [44, 408],
		15: [44, 349],
		16: [44, 291],
		17: [44, 233],
		18: [44, 175],
		19: [44, 117],
		20: [44, 44],
		21: [117, 44],
		22: [175, 44],
		23: [233, 44],
		24: [291, 44],
		25: [349, 44],
		26: [408, 44],
		27: [466, 44],
		28: [524, 44],
		29: [583, 44],
		30: [656, 44],
		31: [656, 117],
		32: [656, 175],
		33: [656, 233],
		34: [656, 291],
		35: [656, 349],
		36: [656, 408],
		37: [656, 466],
		38: [656, 524],
		39: [656, 583]
		}

	def put_player(self, player):
		if player.number == 1:
			return self.positions[player.position][0] + 22, self.positions[player.position][1] + 14
		elif player.number == 2:
			return self.positions[player.position][0] + 22, self.positions[player.position][1] - 14
		elif player.number == 3:
			return self.positions[player.position][0] - 22, self.positions[player.position][1] + 14
		elif player.number == 4:
			return self.positions[player.position][0] - 22, self.positions[player.position][1] - 14




# screen.blit(image, (0,0))