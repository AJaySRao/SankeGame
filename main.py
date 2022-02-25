from turtle import Turtle, Screen
from snake import Snake
import time

s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.tracer(0)

snake = Snake()

s.listen()
game = True

s.onkey(key='Up', fun=snake.move_up)
s.onkey(key='Down', fun=snake.move_down)
s.onkey(key='Left', fun=snake.move_left)
s.onkey(key='Right', fun=snake.move_right)

while game:
    s.update()
    time.sleep(0.1)
    snake.move()










s.exitonclick()