import random
import os


BOARD = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def print_board(b):
    os.system('cls')
    for row in b:
        for item in row:
            print(item, end=' ')
        print()
        

def put_ship(tab):
    row = random.randint(0, len(tab)-1)
    column = random.randint(0, len(tab[row])-1)
    return row, column
    
    
def get_coordinates(tab):
    while True:
        while True:
            row = input('Choose what row you believe is the ship?(with numbers)\n')
            if row.isdigit():
                row = int(row)
                row -= 1
                if 0 <= row < len(tab):
                    break
        while True:
            column = input('Choose what column you believe is the ship?(with numbers)\n')
            if column.isdigit():
                column = int(column)
                column -= 1
                if 0 <= column < len(tab[row]):
                    break
        if tab[row][column] == 'x':
            player_intention = input('It\'s the same than one of you another choose')
        else:
            return row, column
                

def game(t):
    print_board(t)
    ship = put_ship(t) 
    player_win = False
    attempts = 10
    while attempts > 0:
        print('\nattempts left: ', attempts)
        player = get_coordinates(t)

        if player != ship:
            input(' - Water - \n')
            t[player[0]][player[1]] = 'x'
            attempts -= 1
        elif player == ship:
            player_win = True
            break
        print_board(t)
        
    if player_win == True:
        input('\nYou Win!!!')
        print('ship is in row: ', player[0] + 1, ',column: ', player[1] + 1)
    elif player_win == False:
        input('\nno attempts left')
        input('You Lose!!!')
        print('ship is in row: ', ship[0] + 1, ',column: ', ship[1] + 1)
        
  
game(BOARD)