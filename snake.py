from turtle import Turtle
POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]


class Snake:

    def __init__(self):
        self.segments = []
        self.snake()
        self.snake_head = self.segments[0]

    def snake(self):
        for position in POS:
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
        self.snake_head.forward(DISTANCE)

    def move_right(self):
        if self.snake_head.heading() != DIRECTIONS[2]:
            self.snake_head.setheading(DIRECTIONS[0])

    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(DIRECTIONS[1])

    def move_left(self):
        if self.snake_head.heading() != DIRECTIONS[0]:
            self.snake_head.setheading(DIRECTIONS[2])

    def move_down(self):
        if self.snake_head.heading() != DIRECTIONS[1]:
            self.snake_head.setheading(DIRECTIONS[3])
