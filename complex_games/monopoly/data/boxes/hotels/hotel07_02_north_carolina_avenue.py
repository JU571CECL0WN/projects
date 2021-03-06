from data.boxes.hotels.hotel_base import HotelBase


class NorthCarolinaAvenue(HotelBase):
	def __init__(self):
		position = 32
		name = 'North Carolina Avenue'
		price = 300
		group = 7
		rental_price = {
		1: 230 ,
		2: 320 ,
		3: 460 ,
		4: 700 ,
		5: 1400
		}
		super().__init__(position, name, price, group, rental_price)

