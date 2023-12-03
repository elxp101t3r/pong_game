from turtle import Screen, Turtle

GAME_MODE = True
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
right_paddle = Turtle()
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.setposition(x=350, y=0)



def go_up():
    the_y = right_paddle.ycor() + 20
    right_paddle.goto(right_paddle.xcor(), the_y)


def go_down():
    the_y = right_paddle.ycor() - 20
    right_paddle.goto(right_paddle.xcor(), the_y)

screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')



while GAME_MODE:
    screen.update()
    
    
screen.exitonclick()
print('Done')