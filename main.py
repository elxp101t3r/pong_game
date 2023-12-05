from window import Window
from scoreboard import ScoreBoard
from ball import Ball
from right_paddle import RightPaddle
from left_paddle import LeftPaddle

GAME_MODE = True
                                                   
window = Window()

score_board = ScoreBoard()
window.screen.listen()
left = LeftPaddle()
ball = Ball()
right = RightPaddle()

window.screen.onkey(right.go_up, 'Up')
window.screen.onkey(right.go_down, 'Down')
window.screen.onkey(left.go_up, 'W')
window.screen.onkey(left.go_down, 'S')

while GAME_MODE:
    window.screen.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
   
window.screen.exitonclick()
       