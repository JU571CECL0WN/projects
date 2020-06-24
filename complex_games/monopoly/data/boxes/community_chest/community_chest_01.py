import random
from data.boxes.community_chest.community_chest_base import CommunityChestBase


class CommunityChest01(CommunityChestBase):
	def __init__(self):
		position = 2
		super().__init__(position)
