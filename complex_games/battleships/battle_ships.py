import turtle
import random
import time

colors = ['white', 'red', 'blue', 'lightgreen', 'yellow', 'black']
font_style = ('Arial', 30)


class Haturtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ship = False
        
    def hide_cursor(self, x, y):
        if self.ship:
            hahaha.win()
        else:
            self.hideturtle()
            hahaha.missiles -= 1
            self.write('- AIGUA -', font=font_style, align='center')
            hahaha.legendary()
            if hahaha.missiles == 0:
                hahaha.lose()
            

class Manager:
    def __init__(self):
        self.matrix = []
        self.missiles = 8
        
    def geneate_board(self):
        for j in range(4):
            lista = []
            for i in range(4):
                lista.append(self.set_turtle(i + 1, j + 1))
            self.matrix.append(lista)
        self.put_ship()
            
    def set_turtle(self, i, j):
        t = Haturtle()
        t.shape('square')
        t.speed(0)
        t.penup()
        t.shapesize(6.7, 6.7)
        t.goto(i, j)
        t.onclick(t.hide_cursor, btn=1)
        return t
    
    def put_ship(self):
        random.choice(self.matrix[random.randint(0, len(self.matrix) - 1)]).ship = True
        
    def lose(self):
        time.sleep(1.5)
        screen.clear()
        screen.setworldcoordinates(-1, -1, 1, 1)
        screen.bgpic()
        
    def win(self):
        screen.clear()
        screen.setworldcoordinates(-1, -1, 1, 1)
        screen.bgpic('ship.gif')
        
        
    def legendary(self):
        ha.clear()
        ha.write('Tirs restants: {0}'.format(self.missiles), font=font_style, align='center')


screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.title('inutils')
screen.bgpic('ocean-poster.gif')
screen.setworldcoordinates(0, 0, 8.5, 5)
hahaha = Manager()
hahaha.geneate_board()
ha = turtle.Turtle()
ha.hideturtle()
ha.speed(0)
ha.penup()
ha.goto(6, 4)
hahaha.legendary()

screen.listen()
screen.mainloop()
