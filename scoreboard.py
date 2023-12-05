from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.goto(-30, 240)
        self.write("{}".format(self.score1), align="center", font=("Arial", 44))
        
        self.goto(30, 240)
        self.write("{}".format(self.score2), align="center", font=("Arial", 44))
        