from data.manager import Manager
import pygame
	
pygame.init()
number_player = 4
monopoly = Manager(number_player)
monopoly.run()
