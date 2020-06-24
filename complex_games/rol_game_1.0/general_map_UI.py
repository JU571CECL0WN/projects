import os

class Map:
    def __init__(self):
        self.player_money_display = 'money: {0}'.format(gamer['equipment']['money'])
        self.house_ui += '''
                             ___________ 
                            |           |
                            |   < 3 >   |
                            |  font de  |
                            |  la vida  |
                            |           |
                             ---     --- 
                                |   |
                                |   |
         ___________         ___|   |___         ___________ 
        |           |       |           |       |           |
        |   < 1 >    =======    Estas    =======    < 2 >   |
        |                                                   |
        |  Batalla   =======    aqui!    =======   botiga   |
        |           |       |           |       |           |
         -----------         ---     ---         -----------
                                |   |
                                |   |
                             ___|   |___
                            |           |
                            |  <  0  >  |
                            |   acabar  |
                            |    joc    |
                            |           |
                             -----------
        '''
        
    def map_printer(self):
        os.system('cls')
        print(self.player_money_display + house_ui)