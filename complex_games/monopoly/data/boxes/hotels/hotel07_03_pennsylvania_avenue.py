from data.boxes.hotels.hotel_base import HotelBase


class PennsylvaniaAvenue(HotelBase):
	def __init__(self):
		position = 34
		name = 'Pennsylvania Avenue'
		price = 320
		group = 7
		rental_price = {
		1: 250 ,
		2: 340 ,
		3: 480 ,
		4: 730 ,
		5: 1440
		}
		super().__init__(position, name, price, group, rental_price)

