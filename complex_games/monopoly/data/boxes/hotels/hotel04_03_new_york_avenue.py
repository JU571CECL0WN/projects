from data.boxes.hotels.hotel_base import HotelBase


class NewYorkAvenue(HotelBase):
	def __init__(self):
		position = 19
		name = 'NewYork Avenue'
		price = 200
		group = 4
		rental_price = {
		1: 160 ,
		2: 230 ,
		3: 350 ,
		4: 550 ,
		5: 1100
		}
		super().__init__(position, name, price, group, rental_price)
