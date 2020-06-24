import random
from slot_machine import SlotMachine
from player import create_players

class Casino:
    def __init__(self):
        self.safe = 0
        self.material = {'slot_machines': []}
        self.players_inside = []
        
    def invest(self, money):
        self.safe += money
        
    def buy_slot_machine(self):
        self.safe -= 5000
        self.material['slot_machines'].append(SlotMachine())
    
    def player_enter(self, player):
        self.players_inside.append(player)
        self.transfer_money(player)
        print('This player entered ' + player.name)
        
    def player_exit(self, player):
        self.transfer_lgs(player)
        self.players_inside.remove(player)
        print('This player is kicked ' + player.name)
        
    def transfer_money(self, player):
        self.safe += player.money
        player.lgs += player.money
        player.money = 0
        
    def transfer_lgs(self, player):
        player.money += player.lgs
        self.safe -= player.lgs
        player.lgs = 0
        
    def player_activity(self, player):
        player_plays = random.choice(list(self.material.keys()))
        if player_plays == 'slot_machines':
            self.manage_slotmachine_game(player)
        
    def manage_slotmachine_game(self, player):
        for machine in self.material['slot_machines']:
            if not machine.in_use:
                machine.in_use = True
                machine.play(player)
                machine.in_use = False
                
    def run_casino(self):
        for i in range(random.randint(100,1000)):
            tokick = []
            for i in range(random.randint(0, 4)):
                self.player_enter(create_players())
            for player in self.players_inside:
                self.player_activity(player)
                if player.lgs < 20:
                    tokick.append(player)
            for player in tokick:
                self.player_exit(player)
            print(self.safe)
                
        