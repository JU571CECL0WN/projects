from data.boxes.hotels.hotel_base import HotelBase


class ParkPlace(HotelBase):
	def __init__(self):
		position = 37
		name = 'Park Place'
		price = 350
		group = 8
		rental_price = {
		1: 270 ,
		2: 360 ,
		3: 510 ,
		4: 740 ,
		5: 1500
		}
		super().__init__(position, name, price, group, rental_price)

