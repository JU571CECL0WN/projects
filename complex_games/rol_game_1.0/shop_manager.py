import shop_UI
import arsenal


def stats_up(arsenal, player_choose):
    for equipment in arsenal.arsenal['equipment'][player_choose]:
        if equipment == 'defence' or equipment == 'HP' or equipment == 'strenght':
            return equipment
        else:
            continue


def shop(gamer):
    possible_options = ['0','1','2','3','4','5','6']
    shop_UI.shop_showcase(gamer)
    player_choose = input('\n>>> ')
    while True:
        if player_choose in possible_options:
            if player_choose == '0':
                break
            else:
                equipment = stats_up(arsenal, player_choose)
                if gamer['equipment']['money'] >= arsenal.arsenal['equipment'][player_choose]['price']:
                    gamer['stats'][equipment] += arsenal.arsenal['equipment'][player_choose][equipment]
                    gamer['equipment']['money'] -= arsenal.arsenal['equipment'][player_choose]['price']
                    input(' - YOU JUST INCREASED {0} (+ {1})'.format(equipment.upper(), arsenal.arsenal['equipment'][player_choose][equipment]))
                else:
                    input(' - YOU NEED MORE MONEY - ')
            shop_UI.shop_showcase(gamer)
            player_choose = input('DO YOU WANT SOMETHNIG MORE?(< 0 > FOR EXIT) \n>>> ')
        elif player_choose not in possible_options:
            break