import random
import uuid

class Player:
    def __init__(self, money=0, name=''):
        self.money = money
        self.lgs = 0
        self.name = name
        self.startmoney = money
    

def create_players():
    return Player(name=uuid.uuid4().hex, money=random.randint(100, 2000))