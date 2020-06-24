def seconds(time, cursor):
	cursor.clear()
	cursor.setheading(90)
	angle = time * (360 / 60)
	cursor.right(angle)
	cursor.forward(150)
	cursor.backward(150)


def minute(time, cursor):
	cursor.clear()
	cursor.setheading(90)
	angle = time * (360 / 60)
	cursor.right(angle)
	cursor.forward(125)
	cursor.backward(125)


def hour(time, cursor):
	cursor.clear()
	cursor.setheading(90)
	angle = time * (360 / 12)
	cursor.right(angle)
	cursor.forward(75)
	cursor.backward(75)
