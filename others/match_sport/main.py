from data.file_manager import FileManager
from data.stats import Stats

a = FileManager()
s = Stats(a.data)
registers, result = s.get_registers_by_team_and_sport('chaofan', 'handball')
for i in registers:
	print(i)
print(result)
