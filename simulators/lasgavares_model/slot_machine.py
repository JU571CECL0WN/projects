import os
from slot import Slot


class SlotMachine:
    def __init__(self):
        self.slots_quantity = 3
        self.slot = []
        self.setup_slots()
        self.rewards = {'7': 777, '€': 100, '#': 10}
        self.cost = 10
        self.in_use = False
        
    def setup_slots(self):
        for i in range(self.slots_quantity):
            self.slot.append(Slot())
    
    def spin(self):
        result = []
        for slot in self.slot:
            result += slot.spin()
        return result
        
    def check_result(self, result):
        for option in result:
            if result[0] != option:
                return False, None
            
        return True, result[0]
    
    def give_reward(self, reward):
        return self.rewards[reward]
    
    def play(self, player):
        if player.lgs >= self.cost:
            player.lgs -= self.cost
            result = self.spin()
            winorlose, reward = self.check_result(result)
            if winorlose:
                player.lgs += self.give_reward(reward)
            


