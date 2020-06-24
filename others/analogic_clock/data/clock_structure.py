def clock_structure(cursor):
	cursor.penup()
	cursor.right(90)
	cursor.forward(200)
	cursor.left(90)
	cursor.pendown()
	for i in range(60):
		cursor.left(90)
		if i % 15 == 0:
			cursor.forward(40)
			cursor.backward(40)
		elif i % 5 == 0:
			cursor.forward(25)
			cursor.backward(25)
		else:
			cursor.forward(10)
			cursor.backward(10)
		cursor.right(90)
		cursor.circle(200, 6)