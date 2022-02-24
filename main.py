from turtle import Turtle, Screen
from snake import Snake
import time

s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.tracer(0)
s.listen()

snake = Snake()
snake.snake()

game = True

s.onkey(key='w', fun=snake.move_up)
s.onkey(key='s', fun=snake.move_down)
s.onkey(key='a', fun=snake.move_left)
s.onkey(key='d', fun=snake.move_right)

while game:
    s.update()
    time.sleep(0.1)
    snake.move()










s.exitonclick()