import turtle

wn = turtle.Screen()
wn.title("Lenny's Pong Game Sheeesh")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B

#Ball






# Main game loop
while True:
    wn.update()

