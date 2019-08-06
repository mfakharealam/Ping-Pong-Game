import turtle

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)    # stops the window from updating

#   1st Paddle
paddle_one = turtle.Turtle()
paddle_one.speed(0)     # speed of animation, '0' for MAX
paddle_one.color("white")
paddle_one.shape("square")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)    # (0, 0) is in middle

#   2nd Paddle
paddle_two = turtle.Turtle()
paddle_two.speed(0)     # speed of animation, '0' for MAX
paddle_two.color("white")
paddle_two.shape("square")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)    # (0, 0) is in middle

#   Ball
ball = turtle.Turtle()
ball.speed(0)     # speed of animation, '0' for MAX
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)    # (0, 0) is in middle


# movement of paddle
def paddle_one_up():
    y = paddle_one.ycor()   # coordinates
    y += 30
    paddle_one.sety(y)


def paddle_one_down():
    y = paddle_one.ycor()   # coordinates
    y -= 30
    paddle_one.sety(y)


def paddle_two_up():
    y = paddle_two.ycor()   # coordinates
    y += 30
    paddle_two.sety(y)


def paddle_two_down():
    y = paddle_two.ycor()   # coordinates
    y -= 30
    paddle_two.sety(y)


# Keyboard Events
window.listen()
# Left one
window.onkeypress(paddle_one_up, 'w')
window.onkeypress(paddle_one_down, 's')
# right one
window.onkeypress(paddle_two_up, 'Up')
window.onkeypress(paddle_two_down, 'Down')

# main loop for the game to run
while True:
    window.update()

