from data.boxes.hotels.hotel_base import HotelBase


class AtlanticAvenue(HotelBase):
	def __init__(self):
		position = 26
		name = 'Atlantic Avenue'
		price = 260
		group = 6
		rental_price = {
		1: 200 ,
		2: 280 ,
		3: 420 ,
		4: 640 ,
		5: 1300
		}
		super().__init__(position, name, price, group, rental_price)
