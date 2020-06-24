import json
import uuid

from flask import Flask, request

from data.game import Game

game = Game()

server = Flask(__name__)

def validation(data):
	if not data.get('id'):
		return return_json('STOP PLEASE')
	if data['id'] not in game.players.values():
		return return_json('Unrecognized identification')

def return_json(message):
	return json.dumps({'message': message})

@server.route('/')
def info():
	information = """
	Welcome 

	GET /stats --> get game stats
	POST /take --> take pieces

	"""
	return str(information)


@server.route('/stats')
def stats():
	response = {
		'players': game.players,
		'current_player': game.current_player,
		'pieces_left': game.pieces_left,
		'winner': game.winner
	}
	'''
	if game.pieces_left < 1:
		message = 'you win'
		return json.dumps(message)
	'''
	return json.dumps(response)

@server.route('/start', methods=['POST'])
def start():
	data = request.json
	message = validation(data)
	if message:
		return message
	if game.start():
		stats()
		return return_json('Started')
	return return_json('Error Starting')


@server.route('/join')
def join():
	player_id = uuid.uuid4().hex
	if not game.ready_for_play():
		game.join_player(player_id)
	else:
		return return_json('no, the server is full')
	return json.dumps({'id': player_id})


@server.route('/leave', methods=['POST'])
def leave():
	data = request.json
	message = validation(data)
	if message:
		return message
	game.leave(data['id'])
	return return_json('You left')


@server.route('/take' , methods=['POST'])
def take():
	data = request.json
	message = validation(data)
	if message:
		return message
	if data.get('take') not in game.valid_numbers:
		return return_json('you only can put 1 or 2')
	if game.take_pieces(data['take'], data['id']):
		return stats()
	return return_json('Now is not your turn')


@server.route('/reset')
def reset():
	game.pieces_left = 15
	return return_json('reseted')
