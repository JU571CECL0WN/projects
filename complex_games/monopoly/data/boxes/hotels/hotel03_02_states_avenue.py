from data.boxes.hotels.hotel_base import HotelBase


class StatesAvenue(HotelBase):
	def __init__(self):
		position = 13
		name = 'States Avenue'
		price = 140
		group = 3
		rental_price = {
		1: 110 ,
		2: 180 ,
		3: 290 ,
		4: 460 ,
		5: 900
		}
		super().__init__(position, name, price, group, rental_price)
