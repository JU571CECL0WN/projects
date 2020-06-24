import os
import random
BOARD = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def print_board(b):
    for row_index in range(len(b)):
        for index in range(len(b[row_index])):
            if index + 1 < len(b[row_index]):
                print(b[row_index][index], end=' | ')
            else:
                print(b[row_index][index])
        if len(b) > row_index + 1:
            print('-'*10)
        else:
            print()

            
def win_combination(BOARD, sign):
    if (BOARD[0][0] == sign and BOARD[0][1] == sign and BOARD[0][2] == sign) or \
    (BOARD[1][0] == sign and BOARD[1][1] == sign and BOARD[1][2] == sign) or \
    (BOARD[2][0] == sign and BOARD[2][1] == sign and BOARD[2][2] == sign) or \
    (BOARD[0][0] == sign and BOARD[1][0] == sign and BOARD[2][0] == sign) or \
    (BOARD[0][1] == sign and BOARD[1][1] == sign and BOARD[2][1] == sign) or \
    (BOARD[0][2] == sign and BOARD[1][2] == sign and BOARD[2][2] == sign) or \
    (BOARD[0][0] == sign and BOARD[1][1] == sign and BOARD[2][2] == sign) or \
    (BOARD[0][2] == sign and BOARD[1][1] == sign and BOARD[2][0] == sign):
        return True


def check_full(b):
    for i in b:
        for y in i: 
            if y == ' ':
                return False
    return True


def get_coordinates(b, player, icon):
    while True:
        while True:
            row = input('Choose what row you put your piece {0}?(with numbers)\n'.format(player))
            if row.isdigit():
                row = int(row)
                row -= 1
                if 0 <= row < len(b):
                    break
        while True:
            column = input('Choose what column you put your piece {0}?(with numbers)\n'.format(player))
            if column.isdigit():
                column = int(column)
                column -= 1
                if 0 <= column < len(b[row]):
                    break
        if b[row][column] != ' ':
            player_intention = input('It\'s the same than one of you another choose')
        else:
            b[row][column] = icon
            return
        
def round_game(board, player, icon):
    os.system('cls')
    print_board(board)
    get_coordinates(board, player, icon)
    full = check_full(board)
    win = win_combination(board, icon)
    if win is True:
        winner = player
        return winner
    elif full is True:
        winner = 'draw'
        return winner
    
def game():
    print('Hello!')
    player_01 = input('What\'s your name?(Player01)\n')
    player_02 = input('What\'s your name?(Player02)\n')
    players = {'0' : [player_01, 'X'], '1' : [player_02, 'O']}
    who_plays = random.randint(0, len(players) - 1)
    while True:
        playing = str(who_plays % len(players))
        winner = round_game(BOARD, players[playing][0], players[playing][1])
        if winner:
            break
        who_plays += 1
    os.system('cls')
    print('THE WINNER IS:\n - {0} - \n'.format(winner))
    print_board(BOARD)


game()      