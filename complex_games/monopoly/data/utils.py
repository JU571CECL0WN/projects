import random
from data import settings 

def roll_dices():
	return sum([random.randint(1,6) for times in range(settings.dices)])