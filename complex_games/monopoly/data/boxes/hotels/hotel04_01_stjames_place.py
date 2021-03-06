from data.boxes.hotels.hotel_base import HotelBase


class StJamesPlace(HotelBase):
	def __init__(self):
		position = 16
		name = 'St.James Avenue'
		price = 180
		group = 4
		rental_price = {
		1: 140 ,
		2: 210 ,
		3: 330 ,
		4: 520 ,
		5: 1000
		}
		super().__init__(position, name, price, group, rental_price)
