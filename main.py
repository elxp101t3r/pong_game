from turtle import Turtle, Screen
from random import choice

GAME_MODE = True

class Window:
    def __init__(self):
        self.color = 'black'
        self.screen = Screen()
        self.screen.bgcolor(self.color)
        self.screen.setup(width=800, height=600)
        self.screen.title('Pong')


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        
          
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()


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
    


class LeftPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=-350, y=0)
        self.showturtle()
        self.r_move = [self.go_up, self.go_down]
    def go_up(self):
        self.the_y = self.ycor() + 20
        self.goto(self.xcor(), self.the_y)
    
    def go_down(self):
        self.the_y = self.ycor() - 20
        self.goto(self.xcor(), self.the_y)
       
        
window = Window()
window.screen.listen()
left = LeftPaddle()
ball = Ball()
right = RightPaddle()

window.screen.onkey(right.go_up, 'Up')
window.screen.onkey(right.go_down, 'Down')
window.screen.onkeypress(choice(left.r_move))

while GAME_MODE:
    window.screen.update()
    

window.screen.exitonclick()
       