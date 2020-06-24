from data.transformer import Transformer

class TransformerFactory:
	def __init__(self):
		self.max_transformers = 10 
		self.material_for_transformer = {'transfornium': 20, 'cybertonium': 21}

	def create_transformer(self, warehouse):
		build_transformer = True

		for m in material_for_transformer:
			amount = getattr(warehouse, m)
			if amount >= self.material_for_transformer[m]:
				setattr(warehouse, m, amount - self.material_for_transformer[m])
			else:
				build_transformer = False
				break

		if build_transformer:
			return Transformers()