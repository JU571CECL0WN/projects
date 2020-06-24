from data.boxes.hotels.hotel_base import HotelBase


class ConnecticutAvenue(HotelBase):
	def __init__(self):
		position = 9
		name = 'Connecticut Avenue'
		price = 120
		group = 2
		rental_price = {
		1: 100 ,
		2: 160 ,
		3: 260 ,
		4: 440 ,
		5: 860
		}
		super().__init__(position, name, price, group, rental_price)
