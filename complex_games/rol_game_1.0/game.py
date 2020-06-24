import os
import sys
import copy

import battle_manager
import player
import enemies
import general_map_UI
import shop_manager

def getname():
    while True:
        name = input('nom: ')
        name.replace(' ', '')
        if name:
            return name
        
        
def get_player_action(gamer):
    possile_action = ['0', '1', '2', '3']
    while True:
        general_map_UI.print_map(gamer)
        if gamer['stats']['HP'] <= 0:
                return '3'
        player_option = input('>>> ')
        if player_option in possile_action:
            return player_option
        
        
def answer_player_action(gamer):
    player_option = get_player_action(gamer)
    if player_option == '0':
        os.system('cls')
        print(' - ADEU - ')
        sys.exit()
    elif player_option == '1':
        enemy = copy.deepcopy(battle_manager.choose_enemy(enemies, gamer))
        battle_manager.battle(gamer, enemy)
    elif player_option == '2':
        shop_manager.shop(gamer)
    elif player_option == '3':
        gamer['stats']['HP'] = gamer['stats']['maxHP']
        input('HAS RECUPERAT LA VIDA')

def run():
    os.system('cls')
    gamer = player.player
    name = getname()
    gamer['name'] = name
    while True:
        answer_player_action(gamer)
            
run()