import os

def shop_showcase(gamer):
    os.system('cls')
    showcase = 'money: {0}'.format(gamer['equipment']['money'])
    showcase += '''
    \n
        _______________________________________________________________
       ||-------------------------------------------------------------||
       ||       < 1 >        |       < 2 >       |        < 3 >       ||
       ||                    |       _____       |                    ||
       ||      /--_--\       |      / ___ \      |     __|_______     ||
       ||     |/|   |\|      |      | \ / |      |    '--|______/     ||
       ||       |___|        |      |_| |_|      |                    ||
       ||                    |                   |                    ||
       ||-------------------------------------------------------------||
       || armour(+5 defence) |  helmet (+10 HP)  |  dagger(+5 attack) ||
       ||  cost: 75          |  cost: 50         |  cost: 75          ||
       ||-------------------------------------------------------------||
       ||       < 4 >        |       < 5 >       |       < 6 >        ||
       ||                    |       _____       |                    ||
       ||      /--_--\       |      / ___ \      |     |_____________ ||
       ||     |/| @ |\|      |      | \ / |      | [===|____________/ ||
       ||       |___|        |      |_|=|_|      |     |              ||
       ||                    |                   |                    ||
       ||-------------------------------------------------------------||
       ||King Dragon Scales  |  Spartan helmet   |  Celestial Sword   ||
       ||(+55 defensa)       |   (+110 HP)       |  (+55 attakc)      ||
       ||costa: 750          |  cost: 500        |  cost: 750         ||
        ---------------------------------------------------------------
        < 0 > Exit
    '''
    print(showcase)                                               