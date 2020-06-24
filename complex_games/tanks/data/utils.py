import math


def check_range(player_position, enemy_position, range_):
	player_x, player_y = player_position
	enemy_x, enemy_y = enemy_position
	return math.sqrt(((enemy_x - player_x) ** 2) + ((enemy_y - player_y) ** 2)) <= range_
