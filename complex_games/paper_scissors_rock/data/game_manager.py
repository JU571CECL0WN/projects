import random
from data.ui_manager import UI

import pygame
import time

pygame.init()

SCREEN_Y = 580
SCREEN_X = 740

SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            mouse_x, mouse_y = event.pos
            if self.rect.collidepoint(mouse_x, mouse_y):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                text_to_return = None

                # Pressed enter - input is done
                if event.key == pygame.K_RETURN:
                    text_to_return = self.text
                    self.text = ''

                # Delete
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

                # Add one character
                else:
                    self.text += event.unicode

                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

                if text_to_return:
                    return text_to_return

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Manager:
    def __init__(self):
        self.player = None
        #self.set_player()
        self.ui = UI()
        self.possible_options = ['paper', 'scissors', 'rock']
        self.text_font = pygame.font.SysFont('Arial', 30)
        self.game_results = []
        self.rounds = 0
        self.colors = {
        'black': (0, 0, 0), 'white': (255, 255, 255), 'brown': (165, 42, 42),
        'pink': (255, 20, 147), 'orange': (255, 165, 0), 'red': (255, 0, 0),
        'yellow': (255, 255, 0), 'green': (0, 255, 0), 'blue':(0, 0, 255)
        }
        
    def imageing(self, pc, player):
        SCREEN.fill((self.colors['white']))
        text1 = self.text_font.render('PC choose:', True, self.colors['black'])
        SCREEN.blit(text1, (180, 100))
        SCREEN.blit(self.ui.game_images[pc], [120, 150])
        text2 = self.text_font.render('Player choose:', True, self.colors['black'])
        SCREEN.blit(text2, (420, 100))
        SCREEN.blit(self.ui.game_images[player], [400, 150])

    def run(self):
        clock = pygame.time.Clock()
        input_box = InputBox(270, 270, 140, 32)
        done = False

        while not done:
            stay_sleep = False
            player_option = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                input_text = input_box.handle_event(event)
                if input_text:
                    player_option = input_text.lower()

            input_box.update()

            SCREEN.fill((self.colors['white']))

            input_box.draw(SCREEN)

            if player_option in self.possible_options:
                pc_option = random.choice(self.possible_options)
                if (player_option == 'scissors' and pc_option == 'paper') or \
                   (player_option == 'papel' and pc_option == 'rock') or \
                   (player_option == 'rock' and pc_option == 'scissors'):
                   game_result = 'win'
                elif (player_option == 'paper' and pc_option == 'scissors') or \
                     (player_option == 'rock' and pc_option == 'paper') or \
                     (player_option == 'scissors' and pc_option == 'rock'):
                     game_result = 'lose'
                else:
                    game_result = 'draw'
                self.rounds += 1
                print('round {}:\n{}\n-----------------------\n'.format(self.rounds, game_result))
                self.game_results.append(game_result)
                self.imageing(pc_option, player_option)
                stay_sleep = True

            pygame.display.flip()
            clock.tick(30)
            if stay_sleep:
                time.sleep(3)

        pygame.quit()
 # TODO: put round in graphics 
 # TODO: win or lose