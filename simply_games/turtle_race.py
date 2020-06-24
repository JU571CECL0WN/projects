import turtle
import random

colors = ['white', 'red', 'blue', 'lightgreen', 'yellow']
radius = 100

screen = turtle.Screen()
screen.setup(777, 500, 100, 100)
screen.title('Nanu is amazing.chinofan')
screen.bgcolor('black')

cursor = turtle.Turtle()
cursor.color('white')
cursor.shape('turtle')
cursor.pensize(3)  # gruix de la linea
cursor.speed(5)  # maxim = 0
cursor2 = turtle.Turtle()
cursor2.color('yellow')
cursor2.shape('turtle')
cursor2.pensize(3)  # gruix de la linea
cursor2.speed(5)
cursor2.hideturtle()
cursor2.penup()
cursor2.goto(0, -radius / 2.6)
cursor2.showturtle()
cursor2.pendown()


def goahead(move):
    cursor.forward(move)    
   

def goahead2(move):
    cursor2.forward(move)
    
    
def turnleft(move):
    cursor.circle(radius - 20, move)

    
def turnright(move):    
    cursor.circle(-radius - 20, move)
    
    
def turnleft2(move):
    cursor2.circle(radius + 20, move)

    
def turnright2(move):    
    cursor2.circle(-radius + 20, move)
    
    
def turtlerace():
    n = 0
    n2 = 0
    input()
    while True:
        move = random.randint(1, 5)
        move2 = random.randint(1, 5)
        n += move
        n2 += move2
        if n < 270:
            turnleft(move)
        elif n < radius * 2 + 270:
            goahead(move)
        elif n < radius * 2 + 540:
            turnright(move)
        elif n < radius * 4 + 270 * 2:
            goahead(move)
        else:
            winner = 'white_turtle'
            break
            
        if n2 < 270:
            turnleft2(move2)
        elif n2 < radius * 2 + 270:
            goahead2(move2)
        elif n2 < radius * 2 + 540:
            turnright2(move2)
        elif n2 < radius * 4 + 270 * 2:
            goahead2(move2)
        else:
            winner = 'yellow_turtle'
            break
    print(winner)
            
            
turtlerace()
turtle.done()
