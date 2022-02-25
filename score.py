from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.S = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.S} ", align='center', font=('Courier', 18, 'normal'))
        self.S += 1

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"G A M E  O V E R", align='center', font=('Arial', 24, 'bold'))