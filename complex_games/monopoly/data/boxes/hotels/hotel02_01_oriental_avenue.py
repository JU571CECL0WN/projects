from data.boxes.hotels.hotel_base import HotelBase


class OrientalAvenue(HotelBase):
	def __init__(self):
		position = 6
		name = 'Oriental Avenue'
		price = 100
		group = 2
		rental_price = {
		1: 80 ,
		2: 140 ,
		3: 240 ,
		4: 410 ,
		5: 800
		}
		super().__init__(position, name, price, group, rental_price)
