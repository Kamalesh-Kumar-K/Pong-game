import turtle
window = turtle.Screen()
window.setup(800,600)
window.bgcolor("black")
window.title("Pong Game")
window.tracer(0)

#Scores
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,260)

pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Ariel",24,"normal"))
#left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380,0)

#Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(380,0)

#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("blue")
ball.penup()
ball.dx= 0.1
ball.dy = 0.1
ball_speed_increment= 0.000005

# moving_paddle
def lp_up():
    if left_paddle.ycor() < 250:  # Check if the paddle is below the upper limit
        left_paddle.sety(left_paddle.ycor() + 20)

def lp_down():
    if left_paddle.ycor() > -240:  # Check if the paddle is above the lower limit
        left_paddle.sety(left_paddle.ycor() - 20)

def rp_up():
    if right_paddle.ycor() < 250:  # Check if the paddle is below the upper limit
        right_paddle.sety(right_paddle.ycor() + 20)

def rp_down():
    if right_paddle.ycor() > -240:  # Check if the paddle is above the lower limit
        right_paddle.sety(right_paddle.ycor() - 20)

window.listen()
window.onkeypress(lp_up,"w")
window.onkeypress(lp_down,"s")
window.onkeypress(rp_up,"Up")
window.onkeypress(rp_down,"Down")

while True:
    window.update()
    # Increase ball speed over time
    print(ball.dy / abs(ball.dy))
    print(ball.dx / abs(ball.dx))
    ball.dx += (ball.dx / abs(ball.dx)) * ball_speed_increment
    ball.dy += (ball.dy / abs(ball.dy)) * ball_speed_increment

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #ball wall collision

    #top wall
    if ball.ycor()>290:
        ball.dy*= -1

    #bottom wall
    elif ball.ycor()<-290:
        ball.dy*= -1

    #right wall
    elif ball.xcor()>390:
        ball.dx*= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Ariel",24,"normal"))

    #left wall
    elif ball.xcor()<-390:
        ball.dx*= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align= "center", font=("Ariel",24,"normal"))

    #ball paddle collision
    if ball.xcor()>360 and ball.ycor()<right_paddle.ycor()+50 and ball.ycor()>right_paddle.ycor()-50:
        ball.setx(360)
        ball.dx*= -1
    elif ball.xcor()<-360 and ball.ycor()<left_paddle.ycor()+50 and ball.ycor()>left_paddle.ycor()-50:
        ball.setx(-360)
        ball.dx*= -1
    