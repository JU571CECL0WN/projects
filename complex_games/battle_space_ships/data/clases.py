from pygame import locals
import pygame
import random

pygame.init()


class Plane:
    def __init__(self):
        self.x = 20
        self.y = 300
        self.speed = 10
        self.image = pygame.image.load('space_ship.png')


class Bullet:
    def __init__(self, x, y):
        self.x = x + 70
        self.y = y + 40
        self.speed = 10
        self.image = pygame.image.load('bullet.jpg')


class Enemy:
    def __init__(self):
        self.x = 1300
        self.y = random.randint(1, 6) * 100
        self.speed = random.randint(1, 5)
        self.image = pygame.image.load('enemy.jpg')


class Game:
    def __init__(self):
        self.enemies_died = 0
        self.difficulty_factor = 0.99
        self.run = True
        self.bullets = []
        self.enemies = []
        self.plane = Plane()
        self.font = pygame.font.SysFont('Arial', 30)


# pygame.mixer.music.load('minionsbanana.mp3')
# pygame.mixer.music.play(-1, 0.2)

FPS = 60
fpsclock = pygame.time.Clock()

game = Game()

screen_size = (1300, 700)
screen = pygame.display.set_mode(screen_size, 1, 32)
pygame.display.set_caption('nanu')
# die_effect = pygame.mixer.Sound()argument effect


colors = {'black': (0, 0, 0), 'white': (255, 255, 255), 'brown': (165, 42, 42),
          'pink': (255, 20, 147), 'orange': (255, 165, 0), 'red': (255, 0, 0),
          'yellow': (255, 255, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

while game.run:
    enemies_bin = []
    bullets_bin = []
    screen.fill(colors['black'])

    for event in pygame.event.get():
        if event.type == locals.QUIT:
            game.run = False

        elif event.type == locals.KEYUP:
            if event.key == locals.K_SPACE:
                bullet = Bullet(game.plane.x, game.plane.y)
                game.bullets.append(bullet)

    keystate = pygame.key.get_pressed()

    if keystate[locals.K_w]:
        if game.plane.y > 5:
            game.plane.y -= game.plane.speed

    if keystate[locals.K_s]:
        if game.plane.y < screen_size[1] - 100:
            game.plane.y += game.plane.speed

    if random.random() > game.difficulty_factor - game.enemies_died / 10000:
        enemy = Enemy()
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
                    bullets_bin.append(bullet)
                    # die_effect.play()
                    game.enemies_died += 1

        game.enemies.clear()

        game.bullets.clear()

    text = game.font.render('Enemies killed: {}'.format(game.enemies_died), False, colors['pink'])
    screen.blit(text, (10, 10))

    pygame.display.update()
    fpsclock.tick(FPS)

# pygame.mixer.music.stop()
pygame.quit()
