from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 3
        self.y_move = 3
        
    def move(self):
        the_x = self.xcor() + self.x_move
        the_y = self.ycor() + self.y_move
        self.goto(the_x, the_y)
             
    def bounce(self):
        self.y_move *= -1