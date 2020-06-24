from data.boxes.trains.railroad_base import RailroadBase


class BORailroad(RailroadBase):
	def __init__(self):
		position = 25
		name = 'B&O Railroad'
		super().__init__(position, name)
