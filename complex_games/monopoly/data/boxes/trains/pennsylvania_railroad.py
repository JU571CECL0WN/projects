from data.boxes.trains.railroad_base import RailroadBase


class PennsylvaniaRailroad(RailroadBase):
	def __init__(self):
		position = 15
		name = 'Pennsylvania Railroad'
		super().__init__(position, name)
