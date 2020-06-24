import random
import os
import time
who_win = None
players_intention = 'yes'

while True:
    playergamemode = input('What did you want to play  - vs computer - or - vs friend - ?(or press E for exit)\n').lower()
    playergamemode = playergamemode.replace(' ', '')
    playergamemode = playergamemode.replace('ersu', '')

    if playergamemode == 'vscomputer':
        player = input('What\'s your name?\n')
        while True:
            pieces = input('How much blocks do you want?\n')
            if pieces.isdigit():
                pieces = int(pieces)
                break

        while True: 
            while True:
                os.system('cls')
                print('Pieces left: {0}'.format(pieces))
                choice = input('{0} please take 1 or 2 pieces\n'.format(player))
                if choice == '1' or choice == '2':
                    choice = int(choice)
                    pieces -= choice
                    if pieces <= 0:
                        winner = player
                        break
                    os.system('cls')
                    input('Pieces left: {0}'.format(pieces))
                    pc_choice = pieces % 3
                    if pc_choice == 0:
                        pc_choice = random.randint(1, 2)
                    input('Computer choice:\n{0}'.format(pc_choice))
                    pieces -= pc_choice
                    if pieces <= 0:
                        winner = 'PC'
                        break
            break

        input(' - Winner is ... - \n - {0} - '.format(winner))

    elif playergamemode == 'vsfriend':
        player_01 = input('What\'s your name?(Player01)\n')
        player_02 = input('What\'s your name?(Player02)\n')

        while players_intention == 'yes':
            while True:
                pieces = input('How much blocks do you want?\n')
                if pieces.isdigit():
                    pieces = int(pieces)
                    break

            while pieces > 0:
                players = {'0' : player_01, '1' : player_02}
                who_plays = random.randint(0, len(players) - 1)
                while True:
                    playing = str(who_plays % len(players))
                    print('Pieces left: {0}'.format(pieces))
                    player_choice = input('{0} please take 1 or 2 pieces\n'.format(playing[0]))
                    if player_choice == '1' or player_choice == '2':
                        player_choice = int(player_choice)
                        break
                pieces -= player_choice
                if pieces == 0:
                    who_win = player_01
                    break

            input(' - Winner is ... - \n - {0} - '.format(who_win))
            
    elif playergamemode == 'e':
        break
    else:
        input('is not possible this thing') 