from data.boxes.hotels.hotel_base import HotelBase


class Boardwalk(HotelBase):
	def __init__(self):
		position = 39
		name = 'Boardwalk'
		price = 400
		group = 8
		rental_price = {
		1: 300 ,
		2: 400 ,
		3: 560 ,
		4: 810 ,
		5: 1600
		}
		super().__init__(position, name, price, group, rental_price)
