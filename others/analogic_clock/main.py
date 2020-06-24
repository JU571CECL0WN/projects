import turtle
from data import clock_hand, clock_time_manager, clock_structure


def cursor_generator(size):
	cursor = turtle.Turtle()
	cursor.hideturtle()
	cursor.pensize(size)
	cursor.speed(0)

	return cursor

screen = turtle.Screen()
cursor = cursor_generator(3)
clock_structure.clock_structure(cursor)

cursor = cursor_generator(2)
cursor2 = cursor_generator(3)
cursor3 = cursor_generator(4)

now = clock_time_manager.time()
clock_hand.seconds(now.second, cursor)
clock_hand.minute(now.minute, cursor2)
clock_hand.hour(now.hour, cursor3)

while True:
	now2 = clock_time_manager.time()

	if now.second != now2.second:
		clock_hand.seconds(now2.second, cursor)

		if now.minute != now2.minute:
			clock_hand.minute(now2.minute, cursor2)

			if now.hour != now2.hour:
				clock_hand.hour(now2.hour, cursor3)

		now = now2

turtle.done()	
