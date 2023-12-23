import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed(15)

col = ("white", "pink", "cyan", "green", "yellow", "blue")
for i in range(300):
    t.pencolor(col[i % 3])
    t.forward(i * 4)
    t.left(121)
    