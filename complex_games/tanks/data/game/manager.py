import pygame
import random
from data.entities.player import Player
from data.entities.enemy import Enemy
from data.entities.bullet import Bullet
from data import config
from data import utils

pygame.init()


class GameManager:
    def __init__(self):
        self.max_entities = 100
        self.screen_size = config.SCREEN_SIZE
        self.screen = pygame.display.set_mode(self.screen_size)
        self.font = pygame.font.SysFont('Arial', 30)
        self.font2 = pygame.font.SysFont('Arial', 60)

        self.FPS = 30
        self.fpsclock = pygame.time.Clock()
        pygame.display.set_caption('spiders')  # name of the window

        self.player = Player()
        self.all_entities = pygame.sprite.Group(self.player)  # sprite group # self.all_entities.add(@sprite)
        self.max_entities = 5
        self.points = 1
        self.result = 'LOSE'

    def play(self):
        while True:
            self.screen.fill(config.COLORS['white'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            key_state = pygame.key.get_pressed()
            if key_state[pygame.K_LEFT]:
                self.player.move_left()
            if key_state[pygame.K_RIGHT]:
                self.player.move_right()
            if key_state[pygame.K_UP]:
                self.player.move_up()
            if key_state[pygame.K_DOWN]:
                self.player.move_down()

            if len(self.all_entities) < 100:
                if random.random() > 1 - ((self.points + 1) * 0.001) or random.random() > 0.99:
                    enemy = Enemy()
                    self.all_entities.add(enemy)

            for entity in self.all_entities:
                if entity.filename == 'bullet.png':
                    entity.flying()
                    entity.check_die(config.SCREEN_SIZE)
                    if entity.owner != self.player and pygame.sprite.collide_mask(entity, self.player):
                        self.player.alive = False
                    for enemy in self.all_entities:
                        if entity.owner == self.player and pygame.sprite.collide_mask(entity, enemy) and enemy.filename == 'enemy.png':
                            enemy.alive = False
                            self.points += 1
                            self.player.atk_speed += 0.01
                            self.player.range += 1
                            entity.alive = False

                if entity.filename == 'enemy.png':
                    entity.move_to_kill(self.player.get_position())
                    if entity.shoot() and utils.check_range(entity.get_position(), self.player.get_position(),
                                                            entity.range):
                        bullet = Bullet(entity, self.player)
                        self.all_entities.add(bullet)

                    if key_state[pygame.K_SPACE]:
                        if utils.check_range(self.player.get_position(), entity.get_position(), self.player.range):
                            if self.player.shoot():
                                bullet = Bullet(self.player, entity)
                                self.all_entities.add(bullet)

                if not entity.alive:
                    self.all_entities.remove(entity)

                if 1 < ((self.points + 1) * 0.001):
                    self.result = 'WIN'
                    self.player.alive = False

            if not self.player.alive:
                self.all_entities.empty()
                text = self.font2.render('YOU {}'.format(self.result), True, config.COLORS['pink'])
                self.screen.blit(text, (config.SCREEN_SIZE[0] / 2, config.SCREEN_SIZE[1] / 2))
                pygame.time.wait(2250)
                break

            text = self.font.render('SCORE: {}'.format(self.points), True, config.COLORS['pink'])
            self.screen.blit(text, (10, 1))

            self.all_entities.draw(self.screen)
            pygame.display.update()
            self.fpsclock.tick(self.FPS)

        pygame.quit()
