import random
import os


def random_num(m, M):
    if m < M:
        return random.randint(m, M)
    
    
def input_num(m, M):
    while True:
        number = input('A number between {0} and {1}\n'.format(m, M))
        if number.isdigit():
            number = int(number)
            if m <= number <= M:
                return number
            
            
def game():
    M = 100
    m = 1
    num_attempt = 7
    computer = random_num(m, M)
    player_win = False
    
    while num_attempt > 0:
        os.system('cls')
        print('Attempts left: ', num_attempt)
        player = input_num(m, M)
        
        if player < computer:
            m = player
            num_attempt -= 1
        elif player > computer:
            M = player
            num_attempt -= 1
        elif player == computer:
            player_win = True
            break
    
    if player_win == True:
        print('You Win!!!')
    elif player_win == False:
        print('You Lose!!!')
        
while True:  
    game()
    player_int = input('E for exit.\n').lower()
    if player_int == 'e':
        break