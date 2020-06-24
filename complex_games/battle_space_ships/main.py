import pygame
from pygame import locals
import random

from data import clases

pygame.init()

FPS = 60
fpsclock = pygame.time.Clock()

game = clases.Game()

screen_size = (1300, 700)
screen = pygame.display.set_mode(screen_size, 1, 32)
pygame.display.set_caption('nanu')

game.loadmusic()
#die_effect = pygame.mixer.Sound()argument effect


colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'brown': (165, 42, 42),
		  'pink': (255, 20, 147), 'orange': (255, 165, 0), 'red': (255, 0, 0),
		  'yellow': (255, 255, 0), 'green': (0, 255, 0), 'blue':(0, 0, 255)}

while game.run:
	enemies_bin = []
	bullets_bin = []
	screen.fill(colors['black'])


	for event in pygame.event.get():
		if event.type == locals.QUIT:
			game.run = False

		elif event.type == locals.KEYUP:
			if event.key == locals.K_SPACE:
				bullet = clases.Bullet(game.plane.x, game.plane.y)
				game.bullets.append(bullet)

	keystate = pygame.key.get_pressed()

	if keystate[locals.K_w]:
		if game.plane.y > 5:
			game.plane.y -= game.plane.speed

	if keystate[locals.K_s]:
		if game.plane.y < screen_size[1] - 100:
			game.plane.y += game.plane.speed


	if random.random() > game.difficulty_factor - game.enemies_died / 10000:
		enemy = clases.Enemy()
		game.enemies.append(enemy)


	screen.blit(game.plane.image, (game.plane.x, game.plane.y))

	for enemy in game.enemies:
		if enemy.x > 0:
			screen.blit(enemy.image, (enemy.x, enemy.y))
			enemy.x -= enemy.speed
		else:
		    game.run = False
		for bullet in game.bullets:
			if bullet.x < 1300:
				screen.blit(bullet.image, (bullet.x, bullet.y))
				bullet.x += bullet.speed
			else:
				if bullet not in bullets_bin:
					bullets_bin.append(bullet)

			if enemy.y < bullet.y < enemy.y + enemy.image.get_size()[1] and \
				bullet.x + bullet.image.get_size()[0] > enemy.x:
				if enemy not in enemies_bin:
					enemies_bin.append(enemy)
					#die_effect.play()
					game.enemies_died += 1

	
	for enemy in enemies_bin:
		game.enemies.remove(enemy)

	for bullet in bullets_bin:
		game.bullets.remove(bullet)

	text = game.font.render('Enemies killed: {}'.format(game.enemies_died), False, colors['pink'])
	screen.blit(text, (10, 10))

	pygame.display.update()
	fpsclock.tick(FPS)

pygame.mixer.music.stop()
pygame.quit()