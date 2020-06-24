import os


def stat_bar(stat, max_stat):
    percent = stat / max_stat
    bar = percent * 20
    bar = int(bar)
    nobar = 20 - bar
    uibar = '[' + ('=' *  bar) + (' ' * nobar) + ']' + ('{0}/{1}'.format(stat, max_stat))
    return uibar


def battle_ui(player, enemy):
    os.system('cls')
    tmp = 'Has trobat un {0}'.format(enemy['name'])
    tmp += '\n' + enemy['name']
    tmp += '\nNIVELL {0}'.format(enemy['stats']['level'])
    if enemy['stats']['HP'] <= 0:
        tmp += '\nvida ' + stat_bar(0, enemy['stats']['maxHP'])
    else:
        tmp += '\nvida ' + stat_bar(enemy['stats']['HP'], enemy['stats']['maxHP'])
    tmp += '\n{0}\n'.format(enemy['drawing'])
    tmp += '#' * 50
    tmp += '\n' + player['name']
    tmp += '\nNIVELL {0}'.format(player['stats']['level'])
    if player['stats']['HP'] <= 0:
        tmp += '\nvida ' + stat_bar(0, player['stats']['maxHP'])
    else:
        tmp += '\nvida ' + stat_bar(player['stats']['HP'], player['stats']['maxHP'])
    print(tmp)