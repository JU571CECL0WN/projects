import random
from data.engine import Engine
from data.transformer_factory import TransformerFactory
from data.warehouse import Warehouse


class Spaceship:
	def __init__(self):
		self.distance = 0
		self.stat = 'On Land'
		self.arsenal = []
		self.warehouse = Warehouse()
		self.transformer_factory = TransformerFactory()
		self.engines = {
		'engine1': Engine()
		'engine2': None
		}
		self.engine2 = None
		self.cost_force_landing = 2
		# self.engine2 = None

	def Force_landing(self):
		self.stat = 'On Land'
		for n in range(self.cost_force_landing):
			transformer = random.choice(self.arsenal)
			self.arsenal.remove(transformer)


	def launch(self):
		for engine in engines:
			if (engine == None) or engine.energy <= 5:  
				print('Not is possible launch, because you don\'t have needed energy')
			elif engine.energy >= 5:
				engine.energy -= 5
				self.stat = 'Flying'




	def navigate(self):
		if engine1
		self.engine1.energy -= 1
		self.distance += 10
		item = random.choice(list(self.warehouse.__dict__))
		setattr(self.warehouse, item, getattr(self.warehouse, item) + random.randint(0, 3))

	def create_transformer(self):
		transformer = self.transformer_factory.create_transformer(self.warehouse)
		if transformer:
			self.arsernal.append(transformer)

	def fix_engine(self, engine):
		engine.fix_engine(self.warehouse)

	def control_panel(self):
		what = f'distance: {self.distance}\n'
		what += f'stat: {self.stat}\n'
		what += f'arsenal: {len(self.arsenal)}\n'
		what += f'warehouse: {self.warehouse.__dict__}\n'
		what += f'engine: {self.engine1.energy}'
		print(what)

	def manage(self):
		self.launch()
		for i in range(101):
			self.navigate()
		self.control_panel()






		