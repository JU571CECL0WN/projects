from data.boxes.hotels.hotel_base import HotelBase


class KentuckyAvenue(HotelBase):
	def __init__(self):
		position = 21
		name = 'Kentucky Avenue'
		price = 220
		group = 5
		rental_price = {
		1: 170 ,
		2: 250 ,
		3: 380 ,
		4: 580 ,
		5: 1160
		}
		super().__init__(position, name, price, group, rental_price)
