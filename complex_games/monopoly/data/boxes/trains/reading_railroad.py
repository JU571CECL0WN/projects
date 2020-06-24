from data.boxes.trains.railroad_base import RailroadBase


class ReadingRailroad(RailroadBase):
	def __init__(self):
		position = 5
		name = 'Reading Railroad'
		super().__init__(position, name)
