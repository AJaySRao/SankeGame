from turtle import Turtle
import random


class Egg(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.move()

    def move(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 265)
        self.goto(x, y)
