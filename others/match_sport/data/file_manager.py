import random

class FileManager:
	def __init__(self):
		self.file_name = 'data\\registers.csv'
		self.data = ''
		self.read_file()
		self.prepare_data()

	def read_file(self):
		file = open(self.file_name, 'r')

		self.data = file.read()

		file.close()

	def prepare_data(self):
		'''
		result = []
		for i in self.data.split('\n'):
			result.append(i.split(','))
		self.data = result
		'''
		self.data = [i.split(',') for i in self.data.split('\n')]

	def save_random_file(self, num_registers):
		sport_names = ['basketball', 'football', 'volleyball', 'handball', 'atlhetism']
		names = ['nanu', 'samuel', 'chaofan', 'xin', 'alison', 'edu']

		file = open(self.file_name, 'w')

		for i in range(num_registers):
			points = str(random.randint(1, 10)) + '-' + str(random.randint(1, 10))
			team1 = random.choice(names)
			team2 = random.choice(names)
			while team1 == team2:
				team2 = random.choice(names)
			content = '{0},{1},{2},{3}{4}'.format(random.choice(sport_names), team1, team2, points, '\n' if i != num_registers - 1	 else '' )
			file.write(content)

		file.close()