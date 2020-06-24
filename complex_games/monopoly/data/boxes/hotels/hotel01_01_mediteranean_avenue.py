from data.boxes.hotels.hotel_base import HotelBase


class MediteraneanAvenue(HotelBase):
	def __init__(self):
		position = 1
		name = 'Mediteranean Avenue'
		price = 60
		group = 1
		rental_price = {
		1: 70 ,
		2: 130 ,
		3: 220 ,
		4: 370 ,
		5: 750
		}
		super().__init__(position, name, price, group, rental_price)
