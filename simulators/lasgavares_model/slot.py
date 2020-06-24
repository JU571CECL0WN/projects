import random


class Slot:
    def __init__(self):
        self.options = ['7', '€', '€', '€', '€', '#', '#', '#', '#', '#', '#']
        
    def spin(self):
        return random.choice(self.options)