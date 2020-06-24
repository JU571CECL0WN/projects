import battle_UI
import enemies
import random

def player_action(valid_options):
    print(('=' * 50) + '\ntria:')
    for num in range(1, len(valid_options)):
        for possible_action in valid_options:
            if valid_options[-1] != possible_action:
                print('< {0} > '.format(num) + possible_action, end= ' | ')
            else:
                print('< {0} > '.format(num + 1) + possible_action)
    while True:
        action = input('>>> ').lower()
        if action.isdigit():    
            if int(action) <= len(valid_options):
                return action
    
    
def choose_enemy(enemies, gamer):
    enemy_number = random.randint(1, 100)
    if gamer['stats']['strenght'] >= 500 or gamer['stats']['defence'] >= 300:
        return enemies.dragon
    elif gamer['stats']['strenght'] >= 50 or gamer['stats']['defence'] >= 15:
        if enemy_number < 15:
            return enemies.dragon
        else:
            return enemies.dinosaur
    else:
        if enemy_number > 80 and enemy_number < 95:
            return enemies.dinosaur
        elif enemy_number > 95:
            return enemies.dragon
        else:
            return enemies.lizard
    

def battle(gamer, enemy):
    valid_options = ['atacar', 'escapar']
    winner = None
    while True:
        battle_UI.battle_ui(gamer, enemy)
        action = player_action(valid_options)
        if action == '1':
            damage = gamer['stats']['strenght'] 
            enemy['stats']['HP'] -= damage
            battle_UI.battle_ui(gamer, enemy)
            input('{0} ha fet {1} dany'.format(gamer['name'], damage))
            if enemy['stats']['HP'] <= 0:
                gamer['equipment']['money'] += enemy['equipment']['money']
                print('L\'enemic a deixat {0} de monedes'.format(enemy['equipment']['money']))
                winner = gamer
                break
            damage = enemy['stats']['strenght'] - gamer['stats']['defence']
            if damage < 0:
                damage = 0
            gamer['stats']['HP'] -= damage
            battle_UI.battle_ui(gamer, enemy)
            input('{0} ha fet {1} dany'.format(enemy['name'], damage))
            if gamer['stats']['HP'] <= 0:
                winner = enemy
                break
        elif action == '2':
            break
    if winner == gamer:
        input(' - HAS MATAT L\'ENEMIC - ')
    elif winner == enemy:
        fail = ' - T\'HA MATAT L\'ENEMIC - '
        fail += '\n - HAS DE ANAR A LA FONT DE LA VIDA - '
        input(fail)
    else:
        input(' - HAS ESCAPAT - ')
    

        