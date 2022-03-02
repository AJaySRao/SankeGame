from turtle import Turtle, Screen
from snake import Snake
import time
from food import Egg
from score import ScoreBoard

s = Screen()
s.setup(600, 600)
s.bgcolor('black')
s.tracer(0)

snake = Snake()
egg = Egg()
score = ScoreBoard()

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

    #When snake eats a egg
    #size of egg is 10/10.
    #Size of snake body each is 20/20.
    #So when the distance of 2 segments is less than 15 there is a chance snake eating the egg .
    #if that happens move the egg to next random position.
    #Increase the count of consumed egg to keep track of the score and increase size of snake.
    if snake.snake_head.distance(egg) <= 15:
        egg.move()
        snake.extend_segment()
        score.score_increase()

    #When snake hits his head to wall
    #Size of screen is set to 600/600
    #So x & y axis are -300 to 300 each
    #Need some space over so that the body actually looks like touching the edges of the screen
    #so cutting of 10/20 each side from 300
    # if the snake head touches any given number then the game stops
    if snake.snake_head.xcor() <= -290 or snake.snake_head.xcor() >= 290 or snake.snake_head.ycor() >= 280 or snake.\
            snake_head.ycor() <= -290:
        score.compare_score()
        snake.reset()
        # score.game_over()
        # game = False

    #When the snake touches its own body
    for snake_body in snake.segments[1:]:
        if snake.snake_head.distance(snake_body) < 10:
            score.compare_score()
            snake.reset()
            # score.game_over()
            # game = False











s.exitonclick()