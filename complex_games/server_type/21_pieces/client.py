import requests

base_url = 'http://127.0.0.1:5000/'

game_url = base_url + 'stats'
take_url = base_url + 'take'
join_url = base_url + 'join'
start_url = base_url + 'start'

class Client:
	def __init__(self):
		self.id = None

	def info(self):
		response = requests.get(base_url)
		pass

	def game_stats(self):
		response = requests.get(game_url)
		print(response.content)

	def take_pieces(self, n):
		data = {
		'take': int(n)
		}
		response = requests.post(take_url, json=data)
		print(response.content)

	def play(self, n):
		self.game_stats()
		self.take_pieces(n)


	def join_server(self):
		response = requests.get(join_url)
		if response.content == 'no, the server is full':
			print(response.content)
		else:
			self.id = response.content
			print(response.json())

	def main(self):
		while True:
			self.game_stats()
			n = input('how much block you want to take? (1 or 2)')
			if n.isdigit():
				self.play(n)



client = Client()
client.join_server()
client.main()

