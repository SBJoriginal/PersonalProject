import turtle
import random

wn = turtle.Screen()
wn.title("Lenny's Pong  Sheeesh")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball

ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx, ball.dy = 0.1, 0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def spacebar():
    score_a, score_b == 0, 0


# def paddle_a_right():
#     x = paddle_a.xcor()
#     x += 20
#     paddle_a.setx(x)
#
#
# def paddle_a_left():
#     x = paddle_a.xcor()
#     x -= 20
#     paddle_a.setx(x)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(spacebar, " ")
# wn.onkeypress(paddle_a_right, "d")
# wn.onkeypress(paddle_a_left, "a")


# Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking outside
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.goto(0, 0)
        ball.dx, ball.dy = 0.1, 0.1
        ball.dy *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        start = random.choices(range(1, 5))
        if start == [1]:
            ball.dx *= -1
        if start == [2]:
            ball.dy *= -1
        if start == [3]:
            ball.dx *= -1
            ball.dy *= -1
        if start == [4]:
            pass

    if ball.xcor() < -390:
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.goto(0, 0)
        ball.dx, ball.dy = 0.1, 0.1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))
        start = random.choices(range(1, 5))
        if start == [1]:
            ball.dx *= -1
        if start == [2]:
            ball.dy *= -1
        if start == [3]:
            ball.dx *= -1
            ball.dy *= -1
        if start == [4]:
            pass

    # Border checking with paddle

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (paddle_b.ycor() - 50) and ball.ycor() < (paddle_b.ycor() + 50):
        ball.dx *= -1
        ball.dx *= 1.2
        ball.dy *= 1.2
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (paddle_a.ycor() - 50) and ball.ycor() < (paddle_a.ycor() + 50):
        ball.dx *= -1
        ball.dx *= 1.2
        ball.dy *= 1.2

    #border checking for paddlesssss
    if paddle_a.ycor() > 250:
        paddle_a.goto(-350, 320)
    if paddle_a.ycor() < -250:
        paddle_a.goto(-350, -250)
    if paddle_b.ycor() > 250:
        paddle_b.goto(350, 250)
    if paddle_b.ycor() < -250:
        paddle_b.goto(350, -250)


    # def win():
    #     win = turtle.Turtle()
    #     win.speed(0)
    #     pen.color("white")
    #     pen.penup()
    #     pen.hideturtle()
    #     pen.goto(0, 0)

    #Player A wins
    # if score_a == 1:
    #     win()
    #     pen.write("Player A wins!", align="center", font=("Courier", 42, "normal"))
    #
    # #Player B wins
    # if score_b == 1:
    #     win()
    #     pen.write("Player B wins!", align="center", font=("Courier", 42, "normal"))





