class Stats:
	def __init__(self, data):
		self.data = data

	def get_registers_by_sport(self, sport):
		'''
		result = []
		for match in self.data:
			if match[0] == sport:
				result.append(match)
		return result
		'''

		return [match for match in self.data if match[0] == sport]

	def get_registers_by_team(self, team):
		return [match for match in self.data if match[1] == team or match[2] == team]

	def get_registers_by_team_and_sport(self, team, sport):
		registers = [match for match in self.data if (match[1] == team or match[2] == team) and match[0] == sport]
		result = {'num_matches': len(registers),
				  'victories': 0,
				  'losses': 0, 
				  'draw': 0}
		for winsses in registers:
			points = [int(n) for n in winsses[3].split('-')]
			win_position = 1 if points[0] > points[1] else 2 if points[0] < points[1] else 0
			if win_position == 0:
				result['draw'] += 1
			elif winsses[win_position] == team:
				result['victories'] += 1
			else:
				result['losses'] += 1

		return registers,result