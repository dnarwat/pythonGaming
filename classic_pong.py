import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Classic Pong")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# paddle pen 1
p_pen1 = turtle.Turtle()
p_pen1.speed(0)
p_pen1.penup()
p_pen1.setposition(-380, 30)
p_pen1.shapesize(5)
p_pen1.pendown()


# main loop
while True:
    wn.update()