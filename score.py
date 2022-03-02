from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.S = 0
        with open("score_sheet.txt") as data:
            old_score = data.read()
        self.HS = int(old_score)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.S} High Score : {self.HS} ", align='center', font=('Courier', 18, 'normal'))

    def score_increase(self):
        self.S += 1
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.setposition(0, 0)
    #     self.write(f"G A M E  O V E R", align='center', font=('Arial', 24, 'bold'))
    #     self.compare_score()

    def compare_score(self):

        if self.S > self.HS:
            self.HS = self.S
            with open('score_sheet.txt', mode='w') as data:
                data.write(f"{self.HS}")
        self.S = 0
        self.update_score()
