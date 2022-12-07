import turtle as t

size = 90
speed = 100
top = 65
x = -400
y = 330
t.bgcolor("green")

for i in range(5):
    for j in range(5):
        t.penup()
        t.goto(x + 150 * j, y - 150 * i)
        t.pendown()
        # rectangle
        t.fillcolor("gray")
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.right(90)
        t.end_fill()
        # triangle
        t.fillcolor("brown")
        t.begin_fill()
        t.left(45)
        t.forward(top)
        t.right(90)
        t.forward(top)
        t.end_fill()
        # door
        t.penup()
        t.right(45)
        t.forward(size)
        t.right(90)
        t.pendown()
        t.fillcolor("brown")
        t.forward(size - size * 0.6)
        t.begin_fill()
        t.right(90)
        t.forward(size - size * 0.4)
        t.left(90)
        t.forward(size - size * 0.7)
        t.left(90)
        t.forward(size - size * 0.4)
        t.end_fill()

        t.left(90)


t.done()