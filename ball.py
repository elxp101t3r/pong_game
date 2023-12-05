from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        
    def move(self):
        the_x = self.xcor() + 3
        the_y = self.ycor() + 3
        self.goto(the_x, the_y)
             