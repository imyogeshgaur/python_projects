import turtle as yogi

yogi.bgcolor("black")
yogi.pensize(2)

def curve():
    for i in range(200):
        yogi.right(1)
        yogi.forward(1)

yogi.speed(0)
yogi.color("red","pink")

yogi.begin_fill()
yogi.left(140)
yogi.forward(111.65)
curve()

yogi.left(120)
curve()
yogi.forward(111.65)
yogi.end_fill()
yogi.hideturtle()
