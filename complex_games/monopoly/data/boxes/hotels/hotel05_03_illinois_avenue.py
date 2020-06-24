from data.boxes.hotels.hotel_base import HotelBase


class IllinoisAvenue(HotelBase):
	def __init__(self):
		position = 24
		name = 'Illinois Avenue'
		price = 240
		group = 5
		rental_price = {
		1: 190 ,
		2: 270 ,
		3: 400 ,
		4: 610 ,
		5: 1200
		}
		super().__init__(position, name, price, group, rental_price)
