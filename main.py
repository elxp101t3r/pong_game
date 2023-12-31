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
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
   
    if ball.xcor() > 380:
       ball.reset_position()
       score_board.left_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.right_point()
       
window.screen.exitonclick()
       