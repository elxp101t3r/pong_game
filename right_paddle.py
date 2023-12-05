from paddles import Paddle

class RightPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=350, y=0)  
        self.showturtle()
    
    def go_up(self):
        self.the_y = self.ycor() + 20
        self.goto(self.xcor(), self.the_y)
    
    def go_down(self):
        self.the_y = self.ycor() - 20
        self.goto(self.xcor(), self.the_y)
    

