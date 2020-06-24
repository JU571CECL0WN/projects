import random
import os


class Fish:
    def __init__(self, name):
        self.energy = 25
        self.depth = 0
        self.whalesseen = 0
        self.name = name
        self.isalive = True
        self.food = 5
        
    def swim(self):
        if self.energy > 5:
            self.depth += 2
            self.energy -= 5
            if self.seewhale():
                input('You see a whale')
                if self.seeshark():
                    input('but you see a shark and the shark eat the whale')
                else:
                    self.whalesseen += 1
            elif self.seeshark():
                input('You see a shark you have a 50% of probabilities to escape')
                isalive = random.random() < 0.5
                if not isalive:
                    input('You die\nate by a shark')
                    return isalive
                else:
                    input('You stay alive')
            elif self.foundfood():
                self.food += 1
                input('You found food')
        else:
            input('YOU DIE\nnot enough energy')
            self.isalive = False
            
            
    
    def eat(self):
        if self.food == 0:
            print('You don\'t have food')
        else:
            self.energy += 10
            self.food -= 1
        
        
    def seewhale(self):
        return random.random() > 0.75
    
    def seeshark(self):
        return random.random() > 0.85
    
    def foundfood(self):
        return random.random() > 0.65
        
    def display_stats(self):
        print('name:{3}\t\tenergy:{0}\ndepth:-{1}\t\twhales seen:{2}\nfoods left:{4}'.format(self.energy, self.depth, self.whalesseen, self.name, self.food))
    
   
name = input('What name do you want to give to your fish?\n')
nemo = Fish(name)

while nemo.isalive:
    os.system('cls')
    nemo.display_stats()
    playermove = input('eat or swim\n').lower()
    if playermove == 'eat':
        nemo.eat()
    elif playermove == 'swim':
        nemo.swim()
    else:
        input('is not possible')
os.system('cls')
input('You have seen {0} whale/s\nYou dive to -{1} m\nYou have {2} foods left\nYour score is {3}\n'.format(nemo.whalesseen, nemo.depth, nemo.food ,nemo.whalesseen * 10 + nemo.depth + nemo.food * 5))