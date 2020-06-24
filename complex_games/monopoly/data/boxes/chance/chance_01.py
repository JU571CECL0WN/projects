import random
from data.boxes.chance.chance_base import ChanceBase


class Chance01(ChanceBase):
	def __init__(self):
		position = 7
		super().__init__(position)