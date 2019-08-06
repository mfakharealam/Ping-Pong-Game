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
paddle_one.penup()
paddle_one.goto(-350, 0)    # (0, 0) is in middle
#   2nd Paddle

#   Ball



# main loop for the game to run
while True:
    window.update()

