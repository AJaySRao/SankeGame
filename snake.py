

from turtle import Turtle
pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []


    def snake(self):
        for position in pos:
            t = Turtle('square')
            t.color('white')
            t.penup()
            t.goto(position)
            self.segments.append(t)

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            x = self.segments[segment - 1].xcor()
            y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x, y)
        self.segments[0].forward(20)

    def move_right(self):
        self.segments[0].setheading(0)

    def move_up(self):
        self.segments[0].setheading(90)

    def move_left(self):
        self.segments[0].setheading(180)

    def move_down(self):
        self.segments[0].setheading(270)










