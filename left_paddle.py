from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()


class LeftPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=-350, y=0)
        self.showturtle()
        
    def go_up(self):
        self.the_y = self.ycor() + 20
        self.goto(self.xcor(), self.the_y)
    
    def go_down(self):
        self.the_y = self.ycor() - 20
        self.goto(self.xcor(), self.the_y)
       
        