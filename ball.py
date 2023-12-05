from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 1
        self.y_move = 1
        
    def move(self):
        the_x = self.xcor() + self.x_move
        the_y = self.ycor() + self.y_move
        self.goto(the_x, the_y)
             
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        self.bounce_x()