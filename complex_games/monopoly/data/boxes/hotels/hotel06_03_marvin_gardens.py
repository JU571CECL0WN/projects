from data.boxes.hotels.hotel_base import HotelBase


class MarvinGardens(HotelBase):
	def __init__(self):
		position = 29
		name = 'Marvin Gardens'
		price = 280
		group = 6
		rental_price = {
		1: 220 ,
		2: 300 ,
		3: 420 ,
		4: 670 ,
		5: 1340
		}
		super().__init__(position, name, price, group, rental_price)
