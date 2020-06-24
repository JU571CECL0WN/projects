from data.boxes.trains.railroad_base import RailroadBase


class ShortLine(RailroadBase):
	def __init__(self):
		position = 35
		name = 'Short Line'
		super().__init__(position, name)
