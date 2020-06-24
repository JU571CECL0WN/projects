import random
from data.boxes.box_base import BoxBase
from data.settings import total_players


class ChanceBase(BoxBase):
    def __init__(self, position):
        self.name = 'Chance'
        super().__init__(position , self.name)
        self.cards = [attr for attr in dir(self) if '__' not in attr and attr.startswith('card_')]

    def choose_card(self):
        card = random.choice(self.cards)
        return getattr(self, card)

    def card_go_to_jail(self, player):
        sentence = 'You do something wrong go, to jail'
        player.cooldown = 3
        player.position = 10
        return sentence

    def card_leave_jail(self, player):
        sentence = 'You leave the Jail (This card will active when you go to jail)'
        player.cooldown =- 3
        return sentence

    def card_moonwalk(self, player):
        sentence = 'Go back 3 boxes'
        for i in range(3):
            if player.position == 0:
                player.position = 40
                continue
            player.position -= 1 
        return sentence

    def card_repairs(self, player):
        sentence = 'You need to do reparations for your hotels, pay 50 dollars for each'
        for hotel in player.possessions:
            player.money -= 50
        return sentence

    def card_start(self, player):
        sentence = 'Go to the start box'
        player.position = 0
        player.money += 200
        return sentence

    def card_bank_pay(self, player):
        sentence = 'The bank pay you adivident, recive 50 dollars'
        player.money += 50
        return sentence

    def card_buildings_segurity(self, player):
        sentence = 'Rescue for the insurance of your buildings, get 150 dollars'
        player.money += 150
        return sentence

    def card_director_of_directors(self, player):
        sentence = 'They choosen you the director of the Board of Directors pay everyone 50 dollars'
        for players in total_players:
            if players != player:
                players.money += 50
                player.money -= 50
        return sentence

    def card_speeding(self, player):
        sentence = 'Penalty of speeding pay 15 dollars'
        player.money -= 15
        return sentence
        