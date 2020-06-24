import random
import time
import os

number_set = ['0','1','2','3','4','5','6','7','8','9']
result_list = ''
pass_level = False
filename = 'High_score.txt'

def chose_number(n, r):
    tmp = random.choice(n)
    r += tmp
    return r


def levelofdifficulty():
    difficulty = input('What difficulty do you want to have(easy or hard)\n').lower()
    if difficulty == 'easy':
        return 3, 'easy'
    elif difficulty == 'hard':
        return 1, 'hard'
    else:
        print('I guess i\'ts hard')
        time.sleep(2)
        return 1, 'hard'


def print_result(r, s):
    os.system('cls')
    for c in r:
        print(c, end=' ')
    print()
    time.sleep(s)
    os.system('cls')


def player_eye():
    n = input('What did you see?\n')
    return n


def round_game(n, r, s):
    r = chose_number(n, r)
    print_result(r, s)
    player = player_eye()
    player = player.replace(' ', '')
    if player == r:
        return True, r
    elif player != r:
        return False, r
    

def savescore(point, player_name, difficulty):
    content = '\n' + str(point) + ',' + player_name + ',' + difficulty
    file = open(filename, 'a')

    file.write(content)

    file.close()

    
def readscore():
    file = open(filename, 'r')
    a = file.read()
    file.close()
    
    score = {'easy': [], 'hard': []}
    a = a.split('\n')
    for player in a:
        a2 = player.split(',')
        if not a2:
            continue
        
        level = a2[2]
        a2.remove(level)
        score[level].append(a2)
        
    return score


def maxscore(score, difficulty):
    best_score = 0
    best_player = None
    for register in score[difficulty]:
        if int(register[0]) > best_score:
            best_score = int(register[0])
            best_player = register[1]
    return best_score, best_player
    
def game(n, r):
    while True:
        player_name = input('name:')
        if player_name != '':
            break
    sleep_time, difficulty = levelofdifficulty()
    point = 0
    while True:
        level, r = round_game(n, r, sleep_time)
        if level is False:
            break
        else:
            point += 1
    savescore(point, player_name, difficulty)
    score = readscore()
    best_score, best_player = maxscore(score, difficulty)
    print(' - WRONG, THE CORRECT NUMBER is : - \n - {0} - '.format(r))
    print(' - CONGRATULATIONS YOUR SCORE IS: - \n - {0} - '.format(point))
    print(' - HIGHEST SCORE IS: - \n - {0} BY {1} - '.format(best_score, best_player))
    
game(number_set, result_list)
# calculator