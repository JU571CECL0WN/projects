from data.boxes.hotels.hotel_base import HotelBase


class VirginiaAvenue(HotelBase):
	def __init__(self):
		position = 14
		name = 'Virginia Avenue'
		price = 160
		group = 3
		rental_price = {
		1: 130 ,
		2: 200 ,
		3: 310 ,
		4: 490 ,
		5: 980
		}
		super().__init__(position, name, price, group, rental_price)
