class Engine:
	def __init__(self):
		self.max_energy = 100
		self.energy = self.max_energy

	def fix(self, material):
		fix_engine = True
		energy_losed = int(self.max_energy - self.energy)
		price_unit = int((1 * energy_losed) / 2)
		price = {
		'titanium': price_unit,
		'aluminium': price_unit,
		'iron': price_unit
		}

		for m in price:
			amount = getattr(warehouse, m)
			if amount >= price[m]:
				setattr(warehouse, m, amount - price[m])
			else:
				build_transformer = False
				break

		if fix_engine:
			self.energy = max_energy
