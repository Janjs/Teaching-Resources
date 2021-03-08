import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paleta A
pala_a = turtle.Turtle()
pala_a.speed(0)
pala_a.shape("square")
pala_a.color("white")
pala_a.shapesize(stretch_wid=5, stretch_len=1)
pala_a.penup()
pala_a.goto(-350, 0)

# Paleta B
pala_b = turtle.Turtle()
pala_b.speed(0)
pala_b.shape("square")
pala_b.color("white")
pala_b.shapesize(stretch_wid=5, stretch_len=1)
pala_b.penup()
pala_b.goto(350, 0)

# Ball
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = -2
bola.dy = 2

# Bolígrafo
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0 Jugador B: 0", align="center",
          font=("Courier", 24, "normal"))

# marcador
marcador_a = 0
marcador_b = 0

# mover pala


def pala_a_up():
    y = pala_a.ycor()
    y += 20
    pala_a.sety(y)


def pala_a_down():
    y = pala_a.ycor()
    y -= 20
    pala_a.sety(y)


def pala_b_up():
    y = pala_b.ycor()
    y += 20
    pala_b.sety(y)


def pala_b_down():
    y = pala_b.ycor()
    y -= 20
    pala_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(pala_a_up, "w")
wn.onkeypress(pala_a_down, "s")
wn.onkeypress(pala_b_up, "Up")
wn.onkeypress(pala_b_down, "Down")

while True:
    wn.update()

    # Mover la bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Comprobar bordes
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        os.system("afplay bounce.wav&")

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        os.system("afplay bounce.wav&")

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        marcador_a += 1
        pen.clear()
        pen.write("Jugador A: {} Jugador B: {}".format(marcador_a, marcador_b), align="center",
                  font=("Courier", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        marcador_b += 1
        pen.clear()
        pen.write("Jugador A: {} Jugador B: {}".format(marcador_a, marcador_b), align="center",
                  font=("Courier", 24, "normal"))

    # Colision con palwa
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < pala_b.ycor() + 40 and bola.ycor() > pala_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1
        os.system("afplay bounce.wav&")

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < pala_a.ycor() + 40 and bola.ycor() > pala_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1
        os.system("afplay bounce.wav&")
